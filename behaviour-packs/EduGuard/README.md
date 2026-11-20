# EduGuard – Schulserver-Schutz

**Version:** 1.0.0  
**Plattform:** Minecraft Education Dedicated Server  
**API-Abhängigkeit:** `@minecraft/server` 2.1.0  
**Status:** **Nicht unter Minecraft Education 26.32 abgenommen. Vor dem Einsatz testen.**

EduGuard setzt serverseitige Regeln für einen Schulserver um. Der hier gespeicherte Quellcode entspricht der bereitgestellten Ausgangsversion. **Die Wirksamkeit unter Education 26.32 wurde nicht nachgewiesen.**

## Was ist vorgesehen?

- **Gesperrte Gegenstände:** u. a. TNT, TNT-Lore, Endkristall, Feuerzeug, Feuerladung, Enderperle, Chorusfrucht, Flüssigkeitsgegenstände und Befehls-/Strukturblöcke; die vollständige Liste steht in [`scripts/config.js`](scripts/config.js). Spender, Werfer, Eis und Frosteis sind freigegeben.
- **Gefüllte Eimer** werden bei nicht privilegierten Spielern gemäß `emptyFilledBuckets` gegen leere Eimer getauscht.
- **Bestimmte Block-Interaktionen** werden bei nicht privilegierten Spielern abgebrochen, einschließlich Betten außerhalb der Oberwelt sowie Interaktionen mit Respawn-Ankern und ausgewählten Administrationsblöcken. Spender und Werfer können bedient werden.
- **Eis und Frosteis** können im spielmechanisch zulässigen Rahmen abgebaut und verwendet werden.
- **Explosionen** werden bei `cancelExplosions: true` allgemein abgebrochen, **auch wenn ein Operator sie verursacht**.
- **Inventar und Nebenhand** werden regelmäßig auf gesperrte Items geprüft (Voreinstellung: jeder Tick). Warnmeldungen werden zeitlich begrenzt.

**Berechtigungen:** Der Code prüft auf das Minecraft-Berechtigungsniveau **Operator**. Operatoren werden von den Item- und Interaktionssperren ausgenommen; es gibt **keine automatische Ausnahme nur für Lehrkräfte**.

**Versionierung:** Die Versionsnummer bleibt **1.0.0**; diese Änderung gehört zur noch nicht für Education 26.32 abgenommenen 1.0.0-Ausgangsversion. Die Freigabe der Spender ist erst nach den unten aufgeführten Sicherheitstests für den Produktiveinsatz bewertet.

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
| Nicht-Operator erhält, platziert und öffnet Spender/Werfer | Gegenstände bleiben verfügbar; Öffnen und Bedienen sind möglich |
| Nicht-Operator verwendet Spender/Werfer in einer Redstone-Anlage | Anlage funktioniert; Verhalten auch mit zuvor befüllten Behältern prüfen |
| Spender mit gefülltem Wasser-/Lavaeimer, TNT oder Feuerladung durch Nicht-Operator auslösen | Prüfen und protokollieren, ob Flüssigkeiten, Feuer oder Explosionen Schutzregeln umgehen; der Inventarfilter kontrolliert keine Behälterinhalte |
| Große Dropper-/Dispenser-Schaltungen betreiben | Prüfen und protokollieren, ob übermäßig viele Gegenstandsentitäten oder Leistungseinbußen auftreten |
| Nicht-Operator verwendet und baut Eis/Frosteis ab | Im spielmechanisch zulässigen Rahmen möglich; Schmelzen, Abbau und Wasserflüsse beobachten |
| Nicht-Operator versucht ein Bett im Nether/End zu verwenden | Interaktion abgebrochen |
| Nicht-Operator hält gesperrtes Item in Nebenhand | Entfernen bzw. Ersetzen |
| Explosion auslösen | Explosion bei `cancelExplosions: true` abgebrochen |
| Operator verwendet sonst gesperrte Items | Item- und Interaktionsbeschränkungen greifen nicht für Operator |
| `cancelExplosions: false` testen | Globaler Explosionsabbruch durch EduGuard ist deaktiviert |
| `config.js` ändern und Server neu starten | Neue Einstellungen nach Neustart wirksam |

**Erst nach bestandenen Tests als aktiv und wirksam bezeichnen.** Ein `AKTIV`-Eintrag im Log allein ist kein Sicherheitsnachweis.

**Teststatus:** Diese Abnahme wurde nicht auf einem separaten Minecraft-Education-26.32-Testserver durchgeführt. Insbesondere das Auslösen vorbefüllter Spender mit Eimern, TNT und Feuerladungen sowie Belastungstests von Redstone-Anlagen stehen aus. Die Freigabe erlaubt diese Blöcke und Interaktionen, bestätigt aber nicht, dass dadurch keine Schutzumgehung oder Leistungsprobleme möglich sind. Tests mit Nicht-Operator und Operator vor dem Einsatz dokumentieren; bei bestätigter relevanter Umgehung Spender bis zu einer gezielten Gegenmaßnahme wieder sperren.

## Grenzen und wichtige Hinweise

- **Kein vollständiger Griefing- oder Zugriffsschutz.** Das Pack deckt nur die im Code definierten Gegenstände, Ereignisse und Interaktionen ab. Bereits platzierte Blöcke, Befehle, alternative Spielmechaniken oder indirekte Änderungen sind damit nicht automatisch ausgeschlossen.
- Der Inventarfilter überwacht Spielerinventare, nicht bereits befüllte Spender oder Werfer. Freigegebene Redstone-Geräte können daher Aktionen auslösen, ohne dass ein Spieler das Item unmittelbar verwendet; der Explosionsschutz allein verhindert keine möglichen Flüssigkeits- oder Feuerschäden.
- Eis und Frosteis können je nach Spielmechanik schmelzen oder Wasser freisetzen. Das Pack blockiert diese Veränderungen nicht.
- Fehlt eines der benötigten `world.beforeEvents`, wirft das Skript absichtlich einen Fehler. Das bedeutet **nicht**, dass der Server anschließend automatisch sicher blockiert: Das Pack kann inaktiv bleiben, während der Server weiterläuft.
- Die API- und Ereignisunterstützung des tatsächlichen **Education-Dedicated-Servers** muss geprüft werden; Bedrock-API-Dokumentation allein beweist die Kompatibilität nicht.
- Häufige Inventarprüfungen (`scanTicks: 1`) können unter Last Leistungsfolgen haben; mit mehreren gleichzeitig angemeldeten Kindern testen.
- Keine sensiblen Serverdaten, Zugangsschlüssel oder die tatsächliche `edu_server_session.json` ins öffentliche GitHub-Repository einchecken.

**Quellcode:** [`manifest.json`](manifest.json) · [`scripts/config.js`](scripts/config.js) · [`scripts/main.js`](scripts/main.js)
