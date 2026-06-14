# Redstone-Übung 1 – Baue deine eigene Geheimtür!

## Lernziel
Die Teilnehmenden bauen eine Redstone-Geheimtür und lernen dabei, wie Informationen in einer Schaltung gespeichert und durch Signale verändert werden.

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
- Wo speichert die Schaltung die Information, ob die Tür offen oder geschlossen ist?
- Welche Aufgabe übernimmt der Komparator?
- Warum darf der Stein nicht sofort wieder zurückwandern?
- Welche zwei Zustände kennt die Schaltung?
- Wie könnte man die Tür mit einem Geheimcode statt mit einem einzelnen Knopf öffnen?
- Wo gibt es außerhalb von Minecraft Geräte, die sich einen Zustand merken müssen?

## Transfer zur Informatik
Die Schaltung demonstriert das Prinzip eines Speichers: Eine Information wird durch einen Zustand dargestellt und kann durch Eingaben verändert werden. Somit soll Dir diese Übung dabei helfen folgende Begriffe aus der Informatik besser zu verstehen. Sie bilden die Grundlage, wie Computer funktionieren:
- Speicherzustände (An und aus)
- Eingabe (Knopfdruck)
- Verarbeitung (Redstone-Steuerung entscheidet, was passiert)
- Ausgabe (Piston öffnet oder schließt die Tür)