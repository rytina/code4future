# Redstone-Übung 1 – Baue deine eigene Geheimtür!

## Lernziel
Die Teilnehmenden bauen eine Redstone-Geheimtür und lernen dabei die Grundlagen von Signalen, Zuständen, Speicherlogik und Redstone-Komponenten kennen.

## Verwendete Bauteile
- Redstone-Staub
- Knöpfe
- Dropper (Auswurfblock)
- Hopper (Trichter)
- Redstone-Fackel
- Komparator
- Repeater
- Sticky Piston (Klebriger Kolben)

## Die Bauteile einfach erklärt
- Redstone-Staub: das Kabel.
- Knopf: sendet einen kurzen Impuls.
- Dropper: wirft ein Item aus.
- Hopper: transportiert Items weiter.
- Redstone-Fackel: liefert dauerhaft Strom.
- Komparator: erkennt, ob ein Item im Dropper liegt.
- Repeater: verstärkt Signale.
- Sticky Piston: bewegt die Türblöcke.

## Funktionsprinzip
Ein einzelner Stein dient als Speicherzustand:

1. Liegt der Stein im Dropper, erkennt der Komparator ihn. Die Tür ist geschlossen.
2. Wird der richtige Knopf gedrückt, wandert der Stein in den Hopper.
3. Der Dropper ist leer, der Komparator erkennt nichts mehr. Die Tür öffnet sich.
4. Von innen wird ein zweiter Knopf gedrückt.
5. Die Redstone-Fackel deaktiviert kurz die Hopper-Sperre.
6. Der Stein wandert zurück in den Dropper.
7. Der Komparator erkennt den Stein erneut und die Tür schließt sich.

## Lerninhalte
- Signale und Impulse
- Zustände (offen/geschlossen)
- Speicherprinzip mit Items
- Sensoren und Aktoren
- Einführung in digitale Logik

## Reflexionsfragen
- Warum merkt sich die Schaltung, ob die Tür offen oder geschlossen ist?
- Welche Aufgabe übernimmt der Komparator?
- Warum wird der Hopper durch die Redstone-Fackel blockiert?
- Wo werden ähnliche Speichermechanismen in Computern verwendet?

## Transfer zur Informatik
Die Schaltung demonstriert grundlegende Konzepte moderner Computersysteme:
- Speicherzustände
- Eingabe (Knopf)
- Verarbeitung (Redstone-Logik)
- Ausgabe (Tür öffnet oder schließt)

Damit bildet die Übung eine Brücke zwischen Minecraft-Redstone und den Grundlagen der Informatik.