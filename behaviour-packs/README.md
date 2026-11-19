# Behaviour Packs für Minecraft Education

Behaviour Packs (Verhaltenspakete) erweitern Minecraft um eigene Regeln und Funktionen. Mit der **Script API** können wir in JavaScript zum Beispiel auf Spieleraktionen reagieren. Hier sammeln wir den Quellcode unserer Pakete für code4future.

> **Wichtig:** Das sind Pakete für Minecraft **Education / Bedrock**, nicht Java-Edition-Plugins für Spigot oder Paper. Ob bestimmte Skriptfunktionen in Minecraft Education und auf dem Education Dedicated Server verfügbar sind, muss mit der verwendeten Version getestet werden.

## Verfügbare Pakete

| Paket | Zweck | Stand |
| --- | --- | --- |
| [EduGuard](EduGuard/) | Gegenstandssperren, Interaktionsschutz und Explosionsschutz für den Schulserver | **1.0.0 – Abnahmetest unter Education 26.32 ausstehend** |

## Ein eigenes Behaviour Pack erstellen

### 1. Ordner anlegen

Für jedes Pack einen neuen Ordner erstellen. Der Name sollte kurz und eindeutig sein. Beispiel:

```text
behaviour-packs/
└── MeinPack/
    ├── manifest.json
    └── scripts/
        └── main.js
```

Die Datei `manifest.json` ist die Beschreibung des Pakets. Die JavaScript-Datei enthält die Funktionen. Weitere Dateien, wie `scripts/config.js` bei EduGuard, können den Code übersichtlicher machen.

### 2. Die Beschreibung (manifest.json) erstellen

Das folgende Grundgerüst zeigt ein skriptfähiges Pack. Es ist ein **Beispiel**, kein fertig installiertes Paket:

```json
{
  "format_version": 2,
  "header": {
    "name": "Mein erstes Pack",
    "description": "Ein einfaches Minecraft-Verhaltenspaket",
    "uuid": "HIER-NEUE-UUID-1",
    "version": [1, 0, 0],
    "min_engine_version": [1, 21, 0]
  },
  "modules": [
    {
      "type": "data",
      "uuid": "HIER-NEUE-UUID-2",
      "version": [1, 0, 0]
    },
    {
      "type": "script",
      "language": "javascript",
      "uuid": "HIER-NEUE-UUID-3",
      "version": [1, 0, 0],
      "entry": "scripts/main.js"
    }
  ],
  "dependencies": [
    { "module_name": "@minecraft/server", "version": "2.1.0" }
  ]
}
```

**Drei verschiedene UUIDs** erzeugen, beispielsweise auf Linux mit `uuidgen` (drei Mal ausführen), und die Platzhalter ersetzen. Die UUIDs von **EduGuard nicht für ein neues Pack wiederverwenden**. Eine UUID identifiziert ein Pack oder ein Modul; die Versionsnummer wird bei Aktualisierungen angepasst.

Die API-Version `2.1.0` ist hier nur ein Beispiel aus EduGuard. Prüfe für deine verwendete Minecraft-Education-Version, ob die gewünschte Version und die verwendeten Funktionen unterstützt werden.

### 3. Das erste JavaScript-Skript schreiben

Die Datei `scripts/main.js` erstellen:

```js
import { world, system } from "@minecraft/server";

system.run(() => {
  world.sendMessage("Hallo von meinem ersten Behaviour Pack!");
});
```

Dieses minimale Beispiel soll nach dem Laden der Welt eine Nachricht an alle anzeigen. Zum Einstieg reicht ein Texteditor; Visual Studio Code ist praktisch.

### 4. Die Dateien prüfen

Im Ordner des neuen Packs:

```bash
python3 -m json.tool manifest.json >/dev/null
node --check scripts/main.js
```

Diese Befehle prüfen die JSON- bzw. JavaScript-Syntax, **nicht** die tatsächliche Minecraft-API-Kompatibilität. `node` ist optional und wird nur zur lokalen Prüfung benötigt; die Skripte laufen in Minecraft, nicht über Node.js.

### 5. Pack auf einem Education Dedicated Server installieren

**Vor Änderungen: Welt sichern und zunächst auf einem Testserver testen.** Das Beispiel geht von einem Server im Ordner `~/minecraft-edu` aus.

1. Den Server beenden.
2. Den Pack-Ordner inklusive `manifest.json` und `scripts/` in das vom Server verwendete Behaviour-Pack-Verzeichnis kopieren. Meist heißt es `behavior_packs`; bei Education-Installationen kann es auch als `Behavior_Packs` erscheinen. **Zuerst den tatsächlich verwendeten Ordner prüfen** und kein zweites Verzeichnis mit abweichender Groß-/Kleinschreibung anlegen.
3. Das Pack mit seiner Header-UUID und Version in der aktiven Welt registrieren. Die Datei liegt üblicherweise unter `worlds/<WELTNAME>/world_behavior_packs.json`. Existierende Pack-Einträge beibehalten!
4. Server starten und die Skriptmeldungen sowie das Verhalten mit einem Testkonto prüfen.

Beispiel für den Inhalt einer **neuen** `world_behavior_packs.json` bei nur einem Pack (bei bestehenden Welten den Eintrag an das vorhandene JSON-Array anhängen):

```json
[
  {
    "pack_id": "9c9e8cf4-2870-4f42-953e-b9c411020945",
    "version": [1, 0, 0]
  }
]
```

Das Beispiel bezieht sich auf **EduGuard**. Für ein neues Pack stattdessen dessen eigene Header-UUID und Version eintragen. Den aktiven Weltnamen aus `server.properties` (`level-name`) ermitteln. Der Serverstandort und die Ordnernamen können je nach Installation abweichen. Eine vorhandene Weltkonfiguration **nicht** durch das Beispiel ersetzen.

### 6. Testen, verbessern und dokumentieren

Mit einem nicht privilegierten Testkonto und gegebenenfalls einem Operator testen. Die erwarteten Ergebnisse notieren und Fehlermeldungen in der Serverkonsole untersuchen. Erst danach im Kurs einsetzen. Nach Änderungen an der Konfiguration von EduGuard ist ein Server-Neustart erforderlich.

## Weiterführende Dokumentation

- [Minecraft: Introduction to Scripting (Microsoft Learn)](https://learn.microsoft.com/en-us/minecraft/creator/documents/scripting/introduction)
- [Minecraft: Manifest und Modul-Abhängigkeiten](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/examples/addonmanifest)
- [Minecraft Education: Dedicated Server einrichten](https://edusupport.minecraft.net/hc/en-us/articles/46370720373908-IT-Admin-Create-Dedicated-Servers)
- [Minecraft Education: Dedicated Server aktualisieren und eigene Packs übernehmen](https://edusupport.minecraft.net/hc/en-us/articles/360047705032-Update-to-a-New-Version-of-Minecraft-Education)
