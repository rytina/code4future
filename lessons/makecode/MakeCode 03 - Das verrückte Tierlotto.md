# MakeCode-Übung 03 - Das verrückte Tier-Lotto!

**Ziel der Übung:** Du programmierst einen Chat-Befehl, der im Hintergrund würfelt. Je nach gewürfelter Zahl regnet es ein anderes Tier vom Himmel!

Dabei lernst du, wie der Computer **Zufallszahlen** zieht, wie er sie sich in einer **Variable** (einer Art Erinnerungs-Kiste) merkt und wie er mit **Wenn-Dann-Regeln** Entscheidungen trifft.

### 🛠️ Schritt 1: Der Startschuss und die Schleife

Damit es richtig Spaß macht, wollen wir gleich 10 Tiere nacheinander spawnen lassen.

1. Hole dir aus der Kategorie *Spieler* den Block **`bei Chat-Befehl`** und nenne ihn `"tierlotto"`.
2. Gehe zu *Schleifen* und ziehe den grünen Block **`[ 10 ] -mal wiederholen`** in deinen Chat-Befehl.

### 📦 Schritt 2: Die Kiste für unsere Glückszahl (Variable)

Jetzt kommt der wichtigste Teil: Wir müssen einmal pro Durchlauf würfeln und dem Computer sagen, dass er sich das Ergebnis in einer Kiste merken soll.

1. Klicke links auf *Variablen* und wähle **`Mache eine Variable...`**. Nenne sie **`würfel`**.
2. Ziehe den Block **`setze [würfel] auf [ 0 ]`** direkt oben in deine grüne Schleife.
3. Gehe zu *Mathematik* und hole dir den lila Block **`wähle eine zufällige Zahl von [ 0 ] bis [ 10 ]`**.
4. Stecke diesen Block genau da ein, wo die `0` in deinem Variablen-Block steht.
5. Ändere die Zahlen, sodass dort steht: **`von [ 1 ] bis [ 6 ]`**.

### 🧠 Schritt 3: Wenn dies, dann das! (Logik)

Jetzt schauen wir in unsere "würfel"-Kiste hinein und prüfen, welche Zahl darin liegt.

1. Gehe zu *Logik* und hole dir den hellblauen Block **`wenn < wahr > dann`**. Setze ihn direkt unter deine Variable (aber noch *in* die grüne Schleife!).
2. Hole dir – ebenfalls aus *Logik* – den spitzen Vergleichs-Block **`< 0 = 0 >`** und setze ihn oben für das Wort `< wahr >` ein.
3. Hole dir aus *Variablen* deinen roten **`würfel`**-Block und setze ihn in die erste Null.
4. Dein fertiger Block sollte jetzt so aussehen: **`wenn < [würfel] = 1 > dann`**

### 🐄 Schritt 4: Lass es regnen!

1. Gehe zu *Kreaturen* und ziehe den lilafarbenen Block **`spawne Tier [Huhn] bei ~0 ~0 ~0`** in deinen `dann`-Bereich.
2. Ändere die mittlere Zahl auf **10** (also: `~0 ~10 ~0`). *Das bedeutet, das Tier erscheint 10 Blöcke hoch genau über deinem Kopf und fällt herunter!*
3. **Der Kopier-Trick:** Klicke mit der *rechten Maustaste* auf deinen hellblauen `wenn`-Block und wähle **Duplizieren**. Hänge den neuen Block direkt unten an den alten dran.
4. Ändere im neuen Block die Zahl auf die **2** und wähle ein anderes Tier aus (z. B. einen Papagei).
5. Wiederhole das Kopieren, bis du für **alle Zahlen von 1 bis 6** ein eigenes Tier eingebaut hast!