#!/usr/bin/env python3
"""Validate the article and prepare a manual Medium synchronization package."""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
ARTICLE = Path("Programmierangebote fuer Kinder und Jugendliche.md")
SYNC_STATE = ROOT / "medium-sync" / "last-synced-commit.txt"
OUTPUT = ROOT / "medium-sync-output"
MARKDOWN_LINK = re.compile(r"(!?\[[^\]]*\]\()([^\s)]+)(\s+[^)]*)?(\))")
HTML_URL = re.compile(r"((?:src|href)=(['\"]))(.*?)\2", re.IGNORECASE)


class ValidationError(ValueError):
    """Raised when an article link cannot be prepared safely."""


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def public_url(destination: str, root: Path, source_path: Path) -> str:
    parsed = urlsplit(destination)
    if parsed.scheme:
        if parsed.scheme.lower() in {"http", "https"} and parsed.netloc:
            return destination
        if parsed.scheme.lower() == "mailto" and parsed.path:
            return destination
        raise ValidationError(f"Unsupported or invalid link: {destination}")

    if not parsed.path:
        if destination.startswith("#"):
            return destination
        raise ValidationError(f"Link has no destination: {destination}")

    local_path = (root / source_path.parent / unquote(parsed.path)).resolve()
    try:
        relative_path = local_path.relative_to(root.resolve())
    except ValueError as error:
        raise ValidationError(f"Relative link escapes the repository: {destination}") from error
    if not local_path.is_file():
        raise ValidationError(f"Relative link does not exist: {destination}")

    public_path = quote(relative_path.as_posix(), safe="/")
    return urlunsplit(
        ("https", "rytina.github.io", f"/code4future/{public_path}", parsed.query, parsed.fragment)
    )


def prepare_markdown(markdown: str, root: Path, source_path: Path = ARTICLE) -> str:
    def replace_markdown_link(match: re.Match[str]) -> str:
        destination = public_url(match.group(2), root, source_path)
        return f"{match.group(1)}{destination}{match.group(3) or ''}{match.group(4)}"

    def replace_html_url(match: re.Match[str]) -> str:
        destination = public_url(match.group(3), root, source_path)
        return f"{match.group(1)}{destination}{match.group(2)}"

    return HTML_URL.sub(replace_html_url, MARKDOWN_LINK.sub(replace_markdown_link, markdown))


def source_commit() -> str:
    return git("log", "-1", "--format=%H", "--", ARTICLE.as_posix())


def pending_diff(confirmed_commit: str, current_commit: str, current_markdown: str) -> str:
    if not confirmed_commit:
        return "".join(
            difflib.unified_diff(
                [],
                current_markdown.splitlines(keepends=True),
                fromfile="/dev/null",
                tofile=f"{current_commit[:12]}:{ARTICLE.as_posix()}",
            )
        )

    try:
        git("cat-file", "-e", f"{confirmed_commit}^{{commit}}")
        git("merge-base", "--is-ancestor", confirmed_commit, current_commit)
        previous_markdown = subprocess.run(
            ["git", "show", f"{confirmed_commit}:{ARTICLE.as_posix()}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except subprocess.CalledProcessError as error:
        raise ValidationError(
            "Der bestätigte Commit fehlt oder liegt nicht vor dem aktuellen Artikel-Commit."
        ) from error

    diff = "".join(
        difflib.unified_diff(
            previous_markdown.splitlines(keepends=True),
            current_markdown.splitlines(keepends=True),
            fromfile=f"{confirmed_commit[:12]}:{ARTICLE.as_posix()}",
            tofile=f"{current_commit[:12]}:{ARTICLE.as_posix()}",
        )
    )
    return diff or "Keine Inhaltsänderungen seit dem bestätigten Medium-Commit."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT)
    output = parser.parse_args().output_dir
    source = ROOT / ARTICLE
    try:
        original_markdown = source.read_text(encoding="utf-8")
        prepared_markdown = prepare_markdown(original_markdown, ROOT)
        current_commit = source_commit()
        confirmed_commit = SYNC_STATE.read_text(encoding="utf-8").strip()
        if confirmed_commit and not re.fullmatch(r"[0-9a-f]{40}", confirmed_commit):
            raise ValidationError("last-synced-commit.txt must contain a full Git commit SHA or be empty.")
        changed_at = git("show", "-s", "--format=%cI", current_commit)
        diff = pending_diff(confirmed_commit, current_commit, original_markdown)
    except (OSError, subprocess.CalledProcessError, ValidationError) as error:
        raise SystemExit(f"Medium sync preparation failed: {error}") from error

    output.mkdir(parents=True, exist_ok=True)
    (output / "article.md").write_text(prepared_markdown, encoding="utf-8")
    (output / "changes.diff").write_text(diff.rstrip() + "\n", encoding="utf-8")
    (output / "sync-checklist.md").write_text(
        "\n".join(
            [
                "# Medium synchronization checklist",
                "",
                f"- Source: `{ARTICLE.as_posix()}` (GitHub `main`)",
                f"- Article commit: `{current_commit}`",
                f"- Article commit time: `{changed_at}`",
                f"- Last confirmed Medium commit: `{confirmed_commit or 'none'}`",
                "- [ ] Review `article.md` and `changes.diff`.",
                "- [ ] Copy the reviewed content into the existing Medium article.",
                "- [ ] Verify title, headings, links, images, lists, formatting, and sources.",
                f"- [ ] After successful review, record `{current_commit}` in "
                "`medium-sync/last-synced-commit.txt` on GitHub `main`.",
                "",
                "Do not mark this commit synchronized if a newer article change is pending. "
                "No Medium credentials are used and no Medium post is created.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Prepared Medium sync package for article commit {current_commit}.")


if __name__ == "__main__":
    main()
