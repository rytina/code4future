# 🤖 MakeCode-Übung 05 – Die Maze Challenge 🧩

**Wer programmiert den schnellsten Agenten?** 🏆  
**Gewinn: 3 Sterne** ⭐⭐⭐

Dein Agent steht in einem **9 × 9 Felder** großen Labyrinth. Zwischen Start und Ziel stehen Hindernisse. Du weißt **vor dem Programmieren nicht**, wo diese Hindernisse später stehen werden!

Deine Mission: **Programmiere Regeln**, damit der Agent Hindernisse erkennt und selbst seinen Weg zum Ziel sucht. Du darfst ihm keine feste Route vorgeben.

> 🧠 **Unser 5-Schritte-Prinzip:** **Denken → Bauen → Fragen → Prüfen → Erklären**  
> Probiere zuerst selbst. Frage nach einem Hinweis, wenn du feststeckst. Erkläre am Ende, warum deine Lösung funktioniert.

## 🎯 Das ist deine Aufgabe

- **Spielfeld:** 9 × 9 begehbare Felder mit einer Außenmauer.
- **Start und Ziel:** bleiben immer am gleichen Platz.
- **Hindernisse:** werden vom Trainer an unbekannten Stellen aufgestellt.
- **Ziel:** Dein Agent soll selbstständig den Zielblock erreichen.
- **Verboten:** Hindernisse abbauen, überspringen oder zum Ziel teleportieren.

So könnte ein Feld von oben aussehen:

```text
###########
#.........#
#.S...#...#
#...#.....#
#.........#
#.....#...#
#..#......#
#.........#
#....#....#
#.......Z.#
#.........#
###########
```

`#` = Mauer oder Hindernis · `S` = Start · `Z` = Ziel · `.` = freies Feld  
*Die Zeichnung ist nur ein Beispiel: Die echten Hindernisse stehen woanders.*

## 📚 Das lernst du

- **Sensoren:** Der Agent kann prüfen, ob vor ihm ein Block steht.
- **Wenn–Dann:** Er kann abhängig von seiner Umgebung entscheiden.
- **Schleifen:** Er kann immer wieder prüfen und weitergehen.
- **Zufall:** Nicht jede Entscheidung muss fest programmiert sein.
- **Algorithmen verbessern:** Du kannst verschiedene Ideen ausprobieren und vergleichen.

## 🧠 Schritt 1 – Denken

Stelle dir vor, **du** gehst mit geschlossenen Augen durch ein Labyrinth und darfst immer nur direkt vor dir fühlen.

**Überlege zuerst:**

1. Was machst du, wenn der Weg vor dir frei ist?
2. Was machst du, wenn dort ein Hindernis steht?
3. Woher weißt du, dass du am Ziel bist?

Erkläre deine Idee einem anderen Kind, **bevor** du die Blöcke programmierst.

## 🏗️ Schritt 2 – Bauen: Ein ganz einfacher Agent

Öffne **Minecraft Education → MakeCode → neues Projekt**.

Baue diese Regeln mit **Blöcken**, nicht mit einer fest eingetragenen Route:

1. **Spieler:** Hole `bei Chat-Befehl "run"` und nenne ihn `"maze"`.
2. **Agent:** Lasse den Agenten **zum Spieler teleportieren**. Stelle dich dafür auf den Start und richte den Agenten passend aus.
3. **Schleifen:** Wiederhole die folgenden Regeln, **solange der Agent keinen Redstone unter sich erkennt**.
4. **Logik:** **Wenn** der Agent **vorne einen Block erkennt**, drehe ihn nach links **oder** rechts.
5. **Sonst:** Lasse den Agenten **einen Schritt vorwärts** gehen.

💡 **Tipp:** In der Kategorie **Agent** gibt es die Blöcke `Agent erkennt Block` und `Agent erkennt Redstone`. Für den Zielblock prüfst du die Richtung **unten**.

**Deine erste Lösung darf noch schlecht sein!** Vielleicht dreht dein Agent immer rechts herum oder entscheidet sich zufällig. Das ist ein Anfang.

<details>
<summary>💡 Hilfe: Eine mögliche einfache Startlösung (erst öffnen, wenn du Hilfe brauchst)</summary>

Die Lösung dreht bei Hindernissen zufällig nach links oder rechts. Sie verwendet **kein Array**.

```blocks
player.onChat("maze", function () {
    agent.teleportToPlayer()
    while (!agent.detect(AgentDetection.Redstone, DOWN)) {
        if (agent.detect(AgentDetection.Block, FORWARD)) {
            if (Math.randomRange(0, 1) == 0) {
                agent.turn(TurnDirection.Left)
            } else {
                agent.turn(TurnDirection.Right)
            }
        } else {
            agent.move(FORWARD, 1)
        }
    }
    player.say("Ziel erreicht!")
})
```

**Achtung:** Es kann passieren, dass der Agent im Kreis läuft. Das ist ein Problem, das du im nächsten Schritt verbessern darfst. Der Trainer kann einen endlosen Versuch stoppen.

</details>

## 🔍 Schritt 3 – Prüfen: Teste deinen Agenten

Starte im Minecraft-Chat den Befehl:

```text
maze
```

Der Trainer stellt nun **einzelne Hindernisse** auf das Spielfeld. Teste, ob der Agent sie erkennt.

Beobachte genau: Geht er gegen einen Block? Dreht er sich im Kreis? Kommt er am Ziel an?

Wenn dein Agent nicht ankommt, ist das **kein Grund aufzugeben**. Du hast gerade einen Fehler gefunden, den du verbessern kannst!

## 🛠️ Schritt 4 – Verbessern

Suche dir **mindestens eine** Verbesserung aus. Du darfst auch eine ganz eigene Lösung erfinden:

- 🟢 **Leicht:** Sorge dafür, dass der Agent nach **jedem Schritt** wieder prüft, ob er am Ziel ist.
- 🟡 **Mittel:** Prüfe auch, ob **links oder rechts** ein Block steht.
- 🟠 **Knifflig:** Überlege dir feste Regeln statt zufälliger Drehungen. Funktionieren sie auf jedem Feld?
- 🔴 **Profi:** Wie könnte sich der Agent **bereits besuchte Felder** merken?

**Wichtig:** Nur weil ein Agent einmal ans Ziel kommt, heißt das nicht, dass sein Algorithmus immer funktioniert. Teste unterschiedliche Hindernisse!

## 🏆 Schritt 5 – Maze Championship!

Jetzt treten die Agenten gegeneinander an!

**Die Regeln:**

1. Alle Programme starten am **gleichen Start**, mit **gleicher Blickrichtung** und **denselben Hindernissen**.
2. Die Hindernisse werden für den Wettbewerb erst **nach dem Programmieren** festgelegt.
3. Jedes Kind erhält **3 Versuche**.
4. Der Trainer stoppt die Zeit vom **Chat-Befehl** bis zum **erreichten Ziel**.
5. Jeder Versuch dauert maximal **60 Sekunden**. Wer das Ziel nicht findet, bekommt für diesen Versuch keine Zeitwertung.
6. **Die schnellste erfolgreiche Zeit gewinnt 3 Sterne!** Bei Gleichstand gibt es einen Entscheidungsdurchlauf.

| Name | Versuch 1 | Versuch 2 | Versuch 3 | Beste Zeit |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## 🗣️ Erklären

Erzähle zum Schluss:

- Welche Regeln hat dein Agent?
- Was hast du verbessert?
- Warum glaubst du, dass dein Agent schneller oder zuverlässiger geworden ist?

**Geschafft!** Du hast nicht einfach nur Befehle aneinandergereiht, sondern einen Algorithmus entwickelt, der **auf unbekannte Hindernisse reagiert**. 🎉

---

### 👩‍🏫 Hinweis für Trainer*innen (60–90 Minuten)

| Zeit (75-Minuten-Variante) | Abschnitt |
|---|---|
| 0–10 Min. | Spielfeld zeigen, Kinder denken selbst über Regeln nach |
| 10–20 Min. | Einfache, bewusst naive Startlösung am Beamer vorführen |
| 20–45 Min. | Eigene MakeCode-Blöcke bauen und verbessern |
| 45–65 Min. | Wettbewerb: drei Zeitmessungen pro Kind |
| 65–75 Min. | Siegerehrung (3 Sterne) und Erklärung |

**Vorbereiten:** Ein 9×9-Feld mit Außenmauer, festem Start und Redstone-Ziel, 5–8 zunächst unbekannte Einzelhindernisse, Beamer und Stoppuhr. Hindernisse erst nach der Programmierphase für den Wettbewerb festlegen und sicherstellen, dass das Ziel erreichbar ist.

**Technik-Hinweis:** Den Startpunkt und die Blickrichtung vor jedem Versuch identisch einstellen; die Beispiel-Lösung teleportiert den Agenten zum Spieler am Start. Den Agenten über dem Ziel-Redstone laufen lassen. Ein Programm kann bei ungeeigneten Regeln endlos suchen: Versuche deshalb spätestens nach 60 Sekunden manuell abbrechen. Wenn ein alter MakeCode-Lauf noch aktiv ist, vor dem nächsten Start stoppen.

**Fairness:** Die Stoppuhr misst auch eventuelle Rechen-/Serververzögerungen; möglichst gleiche Gerätebedingungen verwenden. Für die Kinder zählt die Bestzeit, nicht zwingend die kürzeste Strecke.

**Mehr zum Thema:** [Offizielles MakeCode-Tutorial „Maze Pathfinding“](https://minecraft.makecode.com/courses/csintro/ai/activity-2). Die Wandfolge-Regel aus dem Tutorial funktioniert nicht bei jeder beliebigen Verteilung einzelner Hindernisse.
