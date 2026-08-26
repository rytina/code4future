# 🤖 MakeCode-Übung 04 – Das Agenten-Navi

Heute bekommt dein Agent ein **Navi**!

Du sagst ihm nicht mehr jeden Schritt einzeln.
Stattdessen bekommt er vorher eine **Route**:

**vor → vor → vor → rechts → vor → vor → vor**

Dann läuft der Agent die Route ganz alleine ab.

> ## 🧠 Regel
>
> **Erst selbst versuchen → dann Hilfe holen → anschließend erklären.**
>
> Fehler sind erlaubt.
> Probier zuerst deine eigene Idee aus!

## 🎯 Deine Mission

Programmiere deinen Agenten so, dass er automatisch ein großes **L** auf den Boden baut.

So ungefähr:

```text
■
■
■
■ ■ ■ ■
```

# 1️⃣ Denken – Welche Route braucht der Agent?

Stell dir vor, du bist selbst der Agent.

Du möchtest ein **L** laufen.

Welche Befehle brauchst du?

Zum Beispiel:

```text
vor
vor
vor
rechts
vor
vor
vor
```

Diese Wörter speichern wir gleich in einer **Liste**.

Eine Liste ist wie ein kleiner **Spickzettel für den Agenten**.

# 2️⃣ Bauen – Erstelle dein Navi

Erstelle einen neuen Chat-Befehl:

```text
navi
```

Ganz am Anfang soll dein Agent:

1. zu dir teleportiert werden
2. Baublöcke bekommen

Zum Beispiel **Diamantblöcke**.

Jetzt brauchen wir die Route.

Gehe zu:

**Fortgeschritten → Arrays**

Dort findest du einen Block mit mehreren Wörtern.

Erstelle eine neue Variable mit dem Namen:

```text
route
```

Trage diese Route ein:

```text
vor
vor
vor
rechts
vor
vor
vor
```

💡 Mit dem kleinen **+** kannst du weitere Wörter hinzufügen.

## 📦 Was ist `route`?

`route` ist der Name unseres Spickzettels.

Darin stehen mehrere Befehle:

```text
["vor", "vor", "vor", "rechts", "vor", "vor", "vor"]
```

Beim Programmieren nennt man so etwas eine **Liste**.

Manchmal hört man dafür auch das Wort **Array**.

# 3️⃣ Der Agent liest den Spickzettel

Jetzt kennt der Agent die Route.

Aber er muss die Wörter noch **nacheinander lesen**.

Gehe zu:

**Schleifen**

und suche:

**Für Element `Wert` von `Liste`**

Ziehe den Block unter deine Route.

Statt **Liste** wählst du:

```text
route
```

Jetzt passiert etwas Spannendes:

Der Agent liest immer **ein Wort nach dem anderen**.

Das Wort, das er gerade liest, heißt:

```text
Wert
```

# 4️⃣ Was bedeutet „vor“?

Jetzt müssen wir dem Agenten erklären:

> Wenn auf meinem Spickzettel **vor** steht, gehe einen Schritt vorwärts.

Hole aus **Logik** einen:

**Wenn ... dann**

Block.

Prüfe:

```text
Wenn Wert = "vor"
```
Dann soll der Agent:

1. **1 Block vorwärts gehen**
2. den Block **unter sich zerstören**
3. dort **einen Block setzen**

So entsteht beim Laufen eine Spur.

# 5️⃣ Was bedeutet „rechts“?

Füge mit dem kleinen **+** hinzu:

**ansonsten wenn**

Prüfe:

```text
Wert = "rechts"
```

Dann soll sich der Agent:

```text
nach rechts drehen
```

Mehr braucht er noch nicht!

# ▶️ Probier dein Navi aus!

Gehe zurück nach Minecraft und schreibe:

```text
navi
```

Beobachte deinen Agenten genau.

### Hat er ein L gebaut?

✅ Ja?

Super! Dein Navi funktioniert.

❌ Nein?

Dann untersuche deinen Code.

* Läuft der Agent in die richtige Richtung?
* Dreht er sich an der richtigen Stelle?
* Sind alle Wörter richtig geschrieben?

# 🔍 Prüfen

Verändere jetzt **nur deine Route**.

Ändere keine anderen Programmblöcke.

Was passiert bei:

```text
vor
vor
rechts
vor
```

Und was passiert bei:

```text
vor
rechts
vor
rechts
vor
```

Probier es aus!

# ⭐ Bonus-Challenge: Das Quadrat

Kannst du deinen Spickzettel so verändern, dass der Agent ein **Quadrat** baut?

Du darfst dafür **keine neuen Programmblöcke** holen.

Du darfst nur die Wörter in deiner `route` verändern oder neue Wörter hinzufügen.

💡 Tipp:

Für ein Quadrat muss der Agent mehrmals:

**laufen → drehen → laufen → drehen**

# 🗣️ Zum Schluss: Erkläre deinen Code

Zeige einem anderen Kind oder einem Trainer deinen Code.

Kannst du diese drei Fragen beantworten?

**1. Was ist `route`?**

**2. Was macht die Schleife?**

**3. Woher weiß der Agent, was `"vor"` und `"rechts"` bedeuten?**

Wenn du das erklären kannst, hast du das **Agenten-Navi verstanden**. 🎉
