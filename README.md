# Museum Duisbyte – Ticketpreis-Rechner

## Funktionen

- Unterstützt **Deutsch und Englisch**  
- Unterschiedliche Preise für Kinder, Jugendliche und Erwachsene  
- Mitgliedschafts-Rabatte: **Premium**, **Basis**, **keine**  
- Premium-Mitglieder können ein Glas Sekt (+0,75 €) hinzufügen  
- Beliebig viele Tickets berechnen  
- Am Ende wird die **Gesamtsumme** und Anzahl der Tickets angezeigt

---

## Projektstruktur – jede Datei hat nur eine Aufgabe

| Datei            | Aufgabe                                                  |
|------------------|----------------------------------------------------------|
| `main.py`        | Startpunkt – hier wird alles gestartet                   |
| `ui.py`          | Benutzeroberfläche (Fragen stellen + Ergebnisse anzeigen)|
| `config.py`      | Alle Preise, Texte, das Logo und Kategorienamen          |
| `calculator.py`  | Berechnet den Preis basierend auf Alter und Optionen     |
| `tickets.py`     | Gibt schöne, lesbare Ticket-Bezeichnungen zurück         |
| `utils.py`       | Hilfsklassen (Enum für Ticket-Typen und Mitgliedschaft)  |

---

## Preisübersicht

| Kategorie                          | Halber Tag | Ganzer Tag |
|------------------------------------|-----------:|-----------:|
| Kinder (0–13 Jahre)                |     2,50 € |     5,00 € |
| Jugendliche (14–17 Jahre)          |     3,50 € |     6,00 € |
| Erwachsene – Premium-Mitglied      |     3,00 € |     6,00 € |
| Erwachsene – Basis-Mitglied        |     4,00 € |     8,00 € |
| Erwachsene – keine Mitgliedschaft  |     5,00 € |    10,00 € |

> **+ Glas Sekt** (nur für Premium-Mitglieder) → **+0,75 €**

---

