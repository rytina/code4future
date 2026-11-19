# EduGuard – Schulserver-Schutz

**Version:** 1.0.0  
**Plattform:** Minecraft Education Dedicated Server  
**API-Abhängigkeit:** `@minecraft/server` 2.1.0  
**Status:** **Nicht unter Minecraft Education 26.32 abgenommen. Vor dem Einsatz testen.**

EduGuard setzt serverseitige Regeln für einen Schulserver um. Der hier gespeicherte Quellcode entspricht der bereitgestellten Ausgangsversion. **Die Wirksamkeit unter Education 26.32 wurde nicht nachgewiesen.**

## Was ist vorgesehen?

- **Gesperrte Gegenstände:** u. a. TNT, TNT-Lore, Endkristall, Feuerzeug, Feuerladung, Enderperle, Chorusfrucht, Spender, Werfer, Befehls-/Strukturblöcke und ausgewählte Eis- bzw. Flüssigkeitsgegenstände; die vollständige Liste steht in [`scripts/config.js`](scripts/config.js).
- **Gefüllte Eimer** werden bei nicht privilegierten Spielern gemäß `emptyFilledBuckets` gegen leere Eimer getauscht.
- **Bestimmte Block-Interaktionen** werden bei nicht privilegierten Spielern abgebrochen, einschließlich Betten außerhalb der Oberwelt und Interaktionen mit Spendern, Werfern, Respawn-Ankern sowie ausgewählten Administrationsblöcken.
- **Eis und frosted ice abbauen** wird bei nicht privilegierten Spielern unterbunden.
- **Explosionen** werden bei `cancelExplosions: true` allgemein abgebrochen, **auch wenn ein Operator sie verursacht**.
- **Inventar und Nebenhand** werden regelmäßig auf gesperrte Items geprüft (Voreinstellung: jeder Tick). Warnmeldungen werden zeitlich begrenzt.

**Berechtigungen:** Der Code prüft auf das Minecraft-Berechtigungsniveau **Operator**. Operatoren werden von den Item- und Interaktionssperren ausgenommen; es gibt **keine automatische Ausnahme nur für Lehrkräfte**.

## Dateien

```text
EduGuard/
├── manifest.json        # Name, Version, UUIDs und benötigte Script API
├── scripts/
│   ├── config.js        # Einstellwerte und Listen gesperrter Gegenstände
│   └── main.js          # Prüfungen und Ereignisbehandlung
└── README.md            # Dokumentation und Abnahme
```

**Konfiguration:** `scripts/config.js` enthält `scanTicks`, `messageCooldownTicks`, `cancelExplosions` und `emptyFilledBuckets`. Änderungen erfordern einen **Server-Neustart**.

## Installation

Die allgemeine [Anleitung für Behaviour Packs](../README.md#5-pack-auf-einem-education-dedicated-server-installieren) beschreibt die Installation. Die UUID für `world_behavior_packs.json` ist:

```json
{ "pack_id": "9c9e8cf4-2870-4f42-953e-b9c411020945", "version": [1, 0, 0] }
```

Zum Beispiel vom geklonten Repository aus:

```bash
SERVER_DIR="$HOME/minecraft-edu"
PACKS_DIR="$SERVER_DIR/behavior_packs" # prüfen: evtl. Behavior_Packs
# Server vorher stoppen und Backup anlegen
test -d "$PACKS_DIR" || echo "Pack-Verzeichnis prüfen!"
cp -r behaviour-packs/EduGuard "$PACKS_DIR/EduGuard"
```

Nur ausführen, nachdem `PACKS_DIR` auf das **tatsächlich verwendete** Pack-Verzeichnis gesetzt wurde. Wird das Pack bereits dort geführt, das bestehende Verzeichnis vor einem Update sichern und bewusst aktualisieren. Zusätzlich muss das Pack in der **aktiven Welt** registriert werden; bloßes Kopieren reicht nicht immer aus.

## Abnahmetest für Minecraft Education 26.32

In einer **separaten Testwelt**, mit **Nicht-Operator** und **Operator**, mindestens folgende Fälle kontrollieren und protokollieren:

| Test | Erwartung gemäß Quellcode |
| --- | --- |
| Pack laden und mit Testkonto beitreten | Startmeldungen; kein Fehler `NICHT AKTIV` / kein API-Importfehler |
| Nicht-Operator erhält TNT oder Endkristall | Entfernen aus Inventar; Nutzung/Interaktion abgebrochen, soweit abgefangen |
| Nicht-Operator erhält einen gefüllten Eimer | Ersetzen durch einen leeren Eimer |
| Nicht-Operator verwendet Feuerzeug oder Feuerladung | Nutzung unterbunden |
| Nicht-Operator benutzt Spender oder Werfer | Interaktion abgebrochen |
| Nicht-Operator versucht Eis abzubauen | Abbau abgebrochen |
| Nicht-Operator versucht ein Bett im Nether/End zu verwenden | Interaktion abgebrochen |
| Nicht-Operator hält gesperrtes Item in Nebenhand | Entfernen bzw. Ersetzen |
| Explosion auslösen | Explosion bei `cancelExplosions: true` abgebrochen |
| Operator verwendet sonst gesperrte Items | Item- und Interaktionsbeschränkungen greifen nicht für Operator |
| `cancelExplosions: false` testen | Globaler Explosionsabbruch durch EduGuard ist deaktiviert |
| `config.js` ändern und Server neu starten | Neue Einstellungen nach Neustart wirksam |

**Erst nach bestandenen Tests als aktiv und wirksam bezeichnen.** Ein `AKTIV`-Eintrag im Log allein ist kein Sicherheitsnachweis.

## Grenzen und wichtige Hinweise

- **Kein vollständiger Griefing- oder Zugriffsschutz.** Das Pack deckt nur die im Code definierten Gegenstände, Ereignisse und Interaktionen ab. Bereits platzierte Blöcke, Befehle, alternative Spielmechaniken oder indirekte Änderungen sind damit nicht automatisch ausgeschlossen.
- Fehlt eines der benötigten `world.beforeEvents`, wirft das Skript absichtlich einen Fehler. Das bedeutet **nicht**, dass der Server anschließend automatisch sicher blockiert: Das Pack kann inaktiv bleiben, während der Server weiterläuft.
- Die API- und Ereignisunterstützung des tatsächlichen **Education-Dedicated-Servers** muss geprüft werden; Bedrock-API-Dokumentation allein beweist die Kompatibilität nicht.
- Häufige Inventarprüfungen (`scanTicks: 1`) können unter Last Leistungsfolgen haben; mit mehreren gleichzeitig angemeldeten Kindern testen.
- Keine sensiblen Serverdaten, Zugangsschlüssel oder die tatsächliche `edu_server_session.json` ins öffentliche GitHub-Repository einchecken.

**Quellcode:** [`manifest.json`](manifest.json) · [`scripts/config.js`](scripts/config.js) · [`scripts/main.js`](scripts/main.js)
