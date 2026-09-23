# 🎮 Commandblock-Übung 01 – Arena-Matchmaking

Stell dir vor, vor eurer Arena liegen zwei Teamflächen: eine **rote** und eine **blaue**. Sobald auf beiden Flächen mindestens ein Spieler steht, startet automatisch ein Countdown. Danach werden beide Teams in die Arena teleportiert.

So ähnlich funktionieren viele Matchmaking-Lobbys in Spielen.

## 🎯 Ziel der Übung

Du baust mit Commandblöcken ein kleines Matchmaking-System:

1. Minecraft erkennt Spieler auf **Team Rot**.
2. Minecraft erkennt Spieler auf **Team Blau**.
3. Die Spieler bekommen automatisch ein Team-Tag.
4. Ein Countdown zählt von **5 bis 0**.
5. Beide Teams werden zu ihren Startpunkten in der Arena teleportiert.

## 📚 Das lernst du

* Wie Minecraft Spieler in einem bestimmten Bereich findet.
* Was ein **Tag** ist.
* Wie ein **Scoreboard** eine Zahl speichern kann.
* Wie ein **Countdown** funktioniert.
* Wie mehrere Commandblöcke zusammenarbeiten.
* Wie man mit Zuständen arbeitet: Warten → Countdown → Match.

# 🏗️ Schritt 1 – Baue die zwei Teamflächen

Baue vor der Arena zwei Flächen, zum Beispiel jeweils **5 × 5 Blöcke**:

```text
        🟥 TEAM ROT                      🟦 TEAM BLAU

        ■ ■ ■ ■ ■                       ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■                       ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■                       ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■                       ■ ■ ■ ■ ■
        ■ ■ ■ ■ ■                       ■ ■ ■ ■ ■
```

Für diese Übung benutzen wir Beispielkoordinaten.

### Rote Fläche

```text
Start: X=-45 Y=28 Z=109
Größe: 5 × 2 × 5
```

Der Bereich wird so ausgewählt:

```mcfunction
@a[x=-45,y=28,z=109,dx=4,dy=1,dz=4]
```

### Blaue Fläche

```text
Start: X=-45 Y=28 Z=100
Größe: 5 × 2 × 5
```

Der Bereich wird so ausgewählt:

```mcfunction
@a[x=-45,y=28,z=100,dx=4,dy=1,dz=4]
```

> 💡 **Wichtig:** `dx=4` bedeutet: Vom Startblock aus werden noch 4 Blöcke weiter geprüft. Zusammen sind das also 5 Blöcke.

# 🔎 Schritt 2 – Teste die Flächen

Hole dir einen Commandblock:

```mcfunction
/give @s command_block
```

Stelle ihn auf:

* **Wiederholen**
* **Bedingungslos**
* **Immer aktiv**

Teste zuerst Team Rot:

```mcfunction
execute if entity @a[x=-45,y=28,z=109,dx=4,dy=1,dz=4] run say Team Rot ist bereit!
```

Stell dich auf die rote Fläche.

Wenn alles funktioniert, sollte Minecraft melden:

```text
Team Rot ist bereit!
```

Teste danach Team Blau genauso.

# 🧮 Schritt 3 – Der Match-Zustand

Unser System muss sich merken können, was gerade passiert.

Wir benutzen dafür ein Scoreboard namens `arena`.

Führe diesen Befehl **einmal** im Chat aus:

```mcfunction
/scoreboard objectives add arena dummy Arena
```

Jetzt legen wir zwei gespeicherte Zahlen an:

```mcfunction
/scoreboard players set #state arena 0
/scoreboard players set #timer arena 0
```

Dabei bedeutet:

```text
#state = 0   → Wir warten auf Spieler
#state = 1   → Countdown läuft
#state = 2   → Match läuft
```

Das Zeichen `#` ist hier nur Teil des Namens. `#state` und `#timer` sind keine echten Spieler.

---

# 🚦 Schritt 4 – Sind beide Teams bereit?

Baue einen neuen Commandblock.

Einstellung:

* **Wiederholen**
* **Bedingungslos**
* **Immer aktiv**

Befehl:

```mcfunction
execute if score #state arena matches 0 if entity @a[x=10,y=64,z=20,dx=4,dy=2,dz=4] if entity @a[x=20,y=64,z=20,dx=4,dy=2,dz=4] run scoreboard players set #state arena 1
```

Dieser Commandblock fragt:

```text
Warten wir gerade?
       ↓
Steht jemand auf Rot?
       ↓
Steht jemand auf Blau?
       ↓
JA → Countdown starten!
```

---

# 🏷️ Schritt 5 – Gib den Spielern Team-Tags

Hinter den letzten Commandblock kommen **Ketten-Commandblöcke**.

Achte darauf, dass die Pfeile der Commandblöcke alle in dieselbe Richtung zeigen.

## Kettenblock 1

* **Kette**
* **Bedingt**
* **Immer aktiv**

```mcfunction
tag @a[x=10,y=64,z=20,dx=4,dy=2,dz=4] add rot
```

## Kettenblock 2

* **Kette**
* **Bedingungslos**
* **Immer aktiv**

```mcfunction
tag @a[x=20,y=64,z=20,dx=4,dy=2,dz=4] add blau
```

Jetzt merkt sich Minecraft:

```text
Spieler auf Rot  → tag = rot
Spieler auf Blau → tag = blau
```

## Kettenblock 3

Setze den Countdown auf 5:

```mcfunction
scoreboard players set #timer arena 5
```

## Kettenblock 4

Zeige die erste Zahl:

```mcfunction
title @a title §e5
```

---

# ⏱️ Schritt 6 – Baue den Countdown

Jetzt bauen wir eine kleine Minecraft-Uhr.

Setze einen **Wiederholungs-Commandblock**.

Einstellungen:

* **Wiederholen**
* **Bedingungslos**
* **Immer aktiv**
* **Verzögerung in Ticks: 20**

> 💡 Minecraft läuft normalerweise mit 20 Ticks pro Sekunde.  
> 20 Ticks sind also ungefähr **1 Sekunde**.

Befehl:

```mcfunction
execute if score #state arena matches 1 if score #timer arena matches 1..5 run scoreboard players remove #timer arena 1
```

Damit wird jede Sekunde 1 abgezogen:

```text
5
↓
4
↓
3
↓
2
↓
1
↓
0
```

---

# 📺 Schritt 7 – Zeige den Countdown an

Hinter die Countdown-Uhr kommen mehrere **Ketten-Commandblöcke**.

Alle:

* **Kette**
* **Bedingungslos**
* **Immer aktiv**

### Zahl 4

```mcfunction
execute if score #timer arena matches 4 run title @a title §e4
```

### Zahl 3

```mcfunction
execute if score #timer arena matches 3 run title @a title §e3
```

### Zahl 2

```mcfunction
execute if score #timer arena matches 2 run title @a title §e2
```

### Zahl 1

```mcfunction
execute if score #timer arena matches 1 run title @a title §e1
```

### LOS!

```mcfunction
execute if score #timer arena matches 0 if score #state arena matches 1 run title @a title §aLOS!
```

---

# 🚀 Schritt 8 – Teleportiere die Teams

Wir benutzen wieder Beispielkoordinaten.

### Spawn Team Rot

```text
X=-30 Y=65 Z=80
```

### Spawn Team Blau

```text
X=30 Y=65 Z=80
```

Hänge weitere Ketten-Commandblöcke an.

### Team Rot

```mcfunction
execute if score #timer arena matches 0 if score #state arena matches 1 run tp @a[tag=rot] -30 65 80
```

### Team Blau

```mcfunction
execute if score #timer arena matches 0 if score #state arena matches 1 run tp @a[tag=blau] 30 65 80
```

### Match-Zustand setzen

Ganz am Ende:

```mcfunction
execute if score #timer arena matches 0 if score #state arena matches 1 run scoreboard players set #state arena 2
```

Damit weiß das System:

```text
Das Match läuft jetzt!
```

---

# 🧩 So arbeitet das ganze System

```text
          WARTEN
             │
             ▼
     Spieler auf ROT?
             │
             ▼
     Spieler auf BLAU?
             │
            JA
             ▼
       TEAM-TAGS SETZEN
             │
             ▼
        COUNTDOWN 5
             │
      4 → 3 → 2 → 1
             │
             ▼
           LOS!
             │
       ┌─────┴─────┐
       ▼           ▼
   TEAM ROT     TEAM BLAU
       │           │
       └─────┬─────┘
             ▼
           ARENA
```

---

# 🧪 Test-Challenge

Teste euer Matchmaking zu zweit.

Prüft nacheinander:

- [ ] Nur ein Spieler steht auf Rot → noch kein Start.
- [ ] Nur ein Spieler steht auf Blau → noch kein Start.
- [ ] Auf beiden Flächen steht jemand → Countdown startet.
- [ ] Die Zahlen 5, 4, 3, 2, 1 erscheinen.
- [ ] Bei `LOS!` werden beide Teams teleportiert.
- [ ] Rot landet am roten Arena-Spawn.
- [ ] Blau landet am blauen Arena-Spawn.

---

# ⭐ Bonus-Challenge 1 – Mehr Spieler pro Team

Was passiert, wenn **zwei Spieler** auf der roten Fläche stehen?

Probiert es aus.

Der Selektor `@a` kann mehrere Spieler gleichzeitig finden.

---

# ⭐ Bonus-Challenge 2 – Countdown abbrechen

Bei unserem ersten System läuft der Countdown weiter, auch wenn ein Spieler seine Fläche wieder verlässt.

Schafft ihr es, das System so zu erweitern, dass der Countdown abgebrochen wird, wenn eines der Teams plötzlich leer ist?

Hinweis:

```mcfunction
execute unless entity ...
```

kann prüfen, ob **kein** passender Spieler gefunden wird.

---

# ⭐ Bonus-Challenge 3 – Match zurücksetzen

Nach dem Match sollen die Tags wieder verschwinden:

```mcfunction
tag @a remove rot
tag @a remove blau
```

Und der Match-Zustand muss wieder auf Warten gesetzt werden:

```mcfunction
scoreboard players set #state arena 0
```

Überlegt euch:

**Wann soll dieser Reset passieren?**

---

# 🧠 Erkläre dein System

Versuche am Ende ohne Hilfe zu erklären:

1. Woran erkennt Minecraft die beiden Teamflächen?
2. Wozu brauchen wir die Tags `rot` und `blau`?
3. Was speichert `#timer`?
4. Warum benutzen wir beim Countdown 20 Ticks?
5. Was bedeuten die drei Werte von `#state`?
6. Warum teleportieren wir die Spieler über ihre Tags und nicht über ihre Position?

Wenn du diese Fragen erklären kannst, hast du nicht nur Commandblöcke gebaut – du hast ein kleines **Spielsystem programmiert**. 🎮
