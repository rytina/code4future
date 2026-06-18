# EduBlocks-Übung 01 – Der kleine Schatzsucher

Kurzbeschreibung
----------------
Story: Ein kleiner Held steht auf einem 5×5‑Raster und soll eine Schatztruhe finden. Die Kinder programmieren Schritt‑für‑Schritt mit EduBlocks, damit der Held Hindernisse umgeht und den Schatz einsammelt.

Zielgruppe
----------
Ca. 8–10 Jahre (auch jüngere Kinder mit Unterstützung)

Dauer
-----
30–45 Minuten

Lernziele
---------
- Reihenfolge von Anweisungen (Sequenzen)
- Wiederholungen (Schleifen)
- Einfache Bedingungen (if)
- Funktionen/Prozeduren (wiederverwendbare Bausteine)
- Basis‑Debugging: schrittweises Testen

Material & Setup
----------------
- EduBlocks im Browser (https://edublocks.org) oder lokale Version
- Optional: micro:bit oder Simulator
- Optional offline: Ausdruck eines 5×5‑Rasters und Spielfiguren
- Vorbereitete Szene: Raster mit Startposition, 1 Schatz, 1–2 Hindernissen

Ablauf (Schritt‑für‑Schritt)
---------------------------
1) Einstieg (5 min)
   - Erzähle die Story: "Unser Held will den Schatz holen, aber auf dem Weg stehen Hindernisse!"
   - Zeige das Raster und die Positionen (Start, Schatz, Hindernis).

2) Demo (5 min)
   - Führe live vor: forward(), forward(), turn_right(), forward() → Schatz.
   - Lass die Kinder vorhersagen, ob es klappt.

3) Aufgabe 1 – Einfache Sequenz (10 min)
   - Ziel: Schreibe eine feste Abfolge von Befehlen, damit der Held zum Schatz kommt.
   - Blöcke: forward(), turn_left(), turn_right().
   - Tipp: Testet nach jedem Block („ein Schritt testen“).

4) Aufgabe 2 – Funktion einführen (5–10 min)
   - Zeige, wie man eine Funktion erstellt, z. B. def gehe(steps): repeat steps: forward()
   - Vorteil: Code bleibt übersichtlich, Aufgaben wiederverwenden.

5) Aufgabe 3 – Hindernis & Bedingung (10 min)
   - Füge ein Hindernis ein (z. B. ein Stein vor dem Weg).
   - Verwende Bedingung: if obstacle_ahead(): turn_right() else: forward()
   - Testen, beobachten, anpassen.

6) Abschluss & Reflexion (5 min)
   - Zeige Lösungsvorschläge, sprecht über Fehlerquellen.

Konkrete Blocks / Beispiel‑Pseudocode
-------------------------------------
- Funktion definieren:
  - def gehe(steps):
      repeat steps:
        forward()

- Hauptprogramm (ein mögliches Beispiel):
  - gehe(2)
  - turn_right()
  - if obstacle_ahead():
      turn_left()
      forward()
      turn_right()
    else:
      forward()
  - if at_treasure():
      pick_up_treasure()

Lehrerhinweise / Tipps
----------------------
- Immer schrittweise testen (nicht sofort 20 Befehle ausführen).
- Visualisiere den Plan zuerst auf Papier (5×5 Raster).
- Wenn nichts funktioniert: Prüft Startrichtung und Schrittanzahl.
- Ermutige lautes Denken: "Warum ist mein Held stecken geblieben?"

Differenzierung / Erweiterungen
--------------------------------
- Einfacher: Kein Hindernis, kürzerer Parcours (z. B. 3×3).
- Schwerer: Zufalls‑Hindernisse, Punkte zählen, Zeitlimit.
- Team‑Challenge: Wer programmiert die kürzeste/robusteste Lösung?
- Anschlussaktivität: Überführung zu MakeCode (gleiche Logik, andere Oberfläche).

Bewertungskriterien (kurz)
--------------------------
- Funktionalität: Kommt der Held sicher zum Schatz?
- Lesbarkeit: Sind Funktionen sinnvoll eingesetzt?
- Robustheit: Reagiert das Programm auf Hindernisse?
- Teamarbeit: Haben alle mitgemacht?

Reflexionsfragen (für Kinder)
-----------------------------
- Was hat am meisten Spaß gemacht?
- Wann hat euer Programm nicht funktioniert — warum?
- Wie habt ihr das Problem gelöst?
- Was würdet ihr beim nächsten Mal anders machen?

Druckbares Material (optional)
------------------------------
- 5×5 Raster‑Vorlage zum Ausdrucken
- Karten mit Block‑Icons (forward, left, right, if, repeat)
- Lösungsblatt mit Beispielreihenfolge

---

Vorschlag Dateiname: lessons/edublocks/EduBlocks 01 - Der kleine Schatzsucher.md
