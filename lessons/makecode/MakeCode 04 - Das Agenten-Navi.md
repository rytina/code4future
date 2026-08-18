# MakeCode-Übung 04 - Das Agenten-Navi

Stell dir vor, dein Agent ist ein ferngesteuertes Auto, und du bist der Navigator. Anstatt ihm jeden Schritt einzeln zu rufen, gibst du ihm vor dem Start einen **Spickzettel** (eine Liste) mit auf den Weg. Der Agent liest den Zettel von oben nach unten und führt alle Befehle automatisch aus!

## 🎯 Ziel der Übung

Du programmierst ein „Navi“ mit einer Liste. Der Agent liest die Liste und baut daraus automatisch die bekannte **L-Form**.

## 📚 Das lernst du

* Was eine **Variable** und eine **Liste (Array)** ist.
* Wie eine **Schleife** eine Liste ausliest.
* Wie der Agent mit **Wenn-Dann-Logik** Entscheidungen trifft.

## 🏗️ Deine Aufgabe

**Den Chat-Befehl und den Spickzettel erstellen:**
Wir brauchen einen neuen Chat-Befehl und unsere Liste. Eine Liste heißt beim Programmieren oft **Array**.

1. Hol dir den Block **Beim Chat-Befehl** und nenne ihn `"navi"`.
2. Gehe zu **Variablen**, klicke auf *Variable erstellen* und nenne sie `route`.
3. Ziehe den Block **Setze 'route' auf** in deinen Chat-Befehl.
4. Gehe zu **Fortgeschritten -> Arrays** und hänge den Block **Array von [ 0, 1, 2 ]** an das Ende deines Variablen-Blocks.
5. Tausche die Zahlen gegen **Texte** aus (unter *Fortgeschritten -> Text*). Schreibe deine Richtungen hinein.

*Tipp für das L:* Deine Liste sollte so aussehen: `["vor", "vor", "vor", "rechts", "vor", "vor", "vor"]` (Tippe auf das kleine `+` am Block, um mehr Platz zu machen).

**Den Agenten die Liste lesen lassen:** Schleifen.
Jetzt hat der Agent den Spickzettel (`route`), aber er muss ihn noch Wort für Wort durchlesen.

1. Gehe zu **Schleifen**.
2. Nimm den Block **Für Element 'Wert' von 'Liste'**.
3. Ziehe diesen Block *unter* deine Liste in den Chat-Befehl.
4. Ändere das Wort `'Liste'` am Ende des Blocks in deine Variable `'route'`.

*Was passiert hier?* Der Agent guckt sich nun nacheinander jedes Wort auf dem Zettel an. Das aktuelle Wort merkt er sich unter dem Namen **'Wert'**.

**Dem Agenten beibringen, was die Wörter bedeuten:** Wenn-Dann Logik.
Der Agent weiß noch nicht, was `"vor"` oder `"rechts"` bedeutet. Das müssen wir ihm mit **Wenn... dann** erklären.

1. Gehe zu **Logik** und ziehe den **Wenn  dann**-Block in deine Schleife.
2. Klicke auf das kleine `+` unten am Block, um ein **ansonsten wenn** hinzuzufügen.
3. Nimm aus **Logik** den Vergleichs-Block `< " " = " " >` und packe ihn in die Wenn-Bedingung.
4. Vergleiche: **Wenn `Wert` = `"vor"` dann:**
* Lass den Agenten einen Block nach *unten* setzen.
* Lass den Agenten *1 Schritt nach vorne* gehen.

5. Vergleiche: **Ansonsten wenn `Wert` = `"rechts"` dann:**
* Lass den Agenten sich nach *rechts* drehen.

## ⭐ Bonus-Challenge für Profis

Wenn dein Agent das "L" erfolgreich baut, versuche Folgendes:

* Kannst du die Liste so verändern, dass der Agent ein **Quadrat** baut, ohne dass du neue Blöcke aus dem Menü holen musst? Du darfst *nur* Wörter in deiner Liste ändern oder hinzufügen!