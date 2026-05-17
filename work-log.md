# Work Log

**Student Name: Vera Schneider** 

---

## Week 1

### Day 1

#### 1. ✅ What did I accomplish?
- Entwicklungsumgebung eingerichtet (VS Code, Git, uv)
- Git installiert und Unterschied zu GitHub gelernt
- uv als neuen Package Manager kennengelernt
- erstes FastAPI Projekt erstellt
- „Hello World“ programmiert
- API im Browser und in /docs getestet
- mehrere einfache Endpoints erstellt
- Hausaufgabe gemacht (Zahl mit +1 addiert)

---

#### 2. 🚧 What challenges did I face?
- Installation von Git auf dem Mac war etwas unübersichtlich
- Homebrew war neu für mich
- am Anfang unsicher, wie alles zusammenhängt (API, Server, Browser)

---

#### 3. 💡 How did I overcome them?
- Hilfe von einem Kommilitonen bei Git und Homebrew bekommen
- durch die ersten kleinen Programme besser verstanden, wie APIs funktionieren


---

### Day 2

#### 1. ✅ What did I accomplish?
- Grundlagen zu APIs, HTTP und JSON gelernt
- mit FastAPI eine eigene Note Taking API erstellt
- POST Endpoint gebaut, um Notizen anzulegen
- GET Endpoint gebaut, um alle Notizen anzuzeigen
- GET Endpoint mit ID erstellt, um einzelne Notizen abzurufen
- Daten mit JSON-Datei gespeichert
- Hausaufgabe eingebaut
- Bonus Challenge eingebaut: Delete Endpoint implementiert

---

#### 2. 🚧 What challenges did I face?
- Internal Server Error beim Erstellen von Notizen
- Probleme beim Speichern in die JSON-Datei
- Unsicherheit, wo genau Code ergänzt werden muss

---

#### 3. 💡 How did I overcome them?
- mit Kommilitone den Fehler im POST Endpoint gefunden (save_notes() hat gefehlt)
- verstanden, dass Daten nach dem Erstellen gespeichert werden müssen
- Code Schritt für Schritt mit der Präsentation verglichen
- ChatGPT genutzt, um Fehlermeldungen zu verstehen und mir Code erklären zu lassen und an richtigen Stellen einzusetzen


---

### Day 3

#### 1. ✅ What did I accomplish?
- Weiteres zu APIs kennengelernt und HTTP-Fehlercodes angeschaut (z. B. 404, 500)
- Unterschied zwischen Path Parameters und Query Parameters gelernt und später zuhause vertieft
- Endpoint @app.get("/queryparameters") erstellt und getestet
- erste Einblicke in automatisiertes Testen (api_test) bekommen
- SQL-Datenbanken angeschaut


Zuhause:
- gesamten bisherigen Code nochmal in Ruhe durchgegangen und besser verstanden, wie eine API aufgebaut ist und, dass für jeden URL-Pfad ein eigener Endpoint definiert werden muss
- Filter-Logik im Code nachvollzogen:
→ mit if-Bedingungen wird geprüft, ob eine Note die Bedingungen erfüllt
→ wenn nicht, wird sie übersprungen (continue)
→ wenn ja, wird sie in die Ergebnisliste aufgenommen
- Unterschied zwischen Path und Query Parameters verstanden:
Path → z. B. /notes/1 → konkrete Ressource
Query → z. B. /notes?category=work → Filter auf mehrere Ergebnisse
- zusätzliche Übung zu Path Parameters gemacht (/test/... Endpoints): verschiedene Varianten getestet
- gelernt, dass die Reihenfolge der Endpoints wichtig ist, weil FastAPI den ersten passenden nimmt
Beispiel: /test/123 wurde zuerst als {value} interpretiert, nach Umstellen der Reihenfolge wurde der feste Endpoint korrekt erkannt
- Tags und Filter erweitert: Tag-Filter implementiert, kombinierte Filter ausprobiert
- erkannt, dass Datenstruktur beim Erstellen korrekt gesetzt werden muss (z. B. tags hinzufügen)
- Code weiter strukturiert: Endpoints nach CRUD-Prinzip sortiert
- Filter-Logik verbessert und erweitert
- Categories- und Tag-Endpunkte ergänzt
- neue Features aus der Hausaufgabe umgesetzt: Top Tags mit Counter, Unique Tags Count, Categories Endpoints, PATCH Endpoint (partielle Updates), Date-Based Filtering
- SQLModel installiert (uv add sqlmodel)
- Code auf Datenbank umgestellt
- Many-to-Many Beziehung zwischen Notes und Tags umgesetzt:
→ Link-Tabelle (NoteTagLink) eingeführt
→ Verknüpfung zwischen Note und Tag hergestellt
→ getestet, ob Tags korrekt gespeichert und geladen werden
- regelmäßig in /docs und über URL-Parameter getestet


---

#### 2. 🚧 What challenges did I face?
- Path vs Query Parameters im Unterricht zunächst nicht vollständig verstanden
- automatisiertes Testen (api_test) im Unterricht nicht gut mitbekommen
- Fehler bei eigenen Endpoints (z. B. Syntaxfehler wie fehlende : oder {})
- unerwartetes Verhalten bei /test/123 wegen falscher Endpoint-Reihenfolge
- Internal Server Error beim Arbeiten mit Tags
- Filter mit Tags und kombinierte Filter haben zunächst keine Ergebnisse geliefert
- Probleme mit notes_db (nicht definiert/falsche Verwendung)
- Verständnisproblem bei verschachtelten Schleifen (Tags innerhalb von Notes)
- Counter zunächst nicht korrekt verwendet (most_common hat nicht funktioniert)
- PATCH Endpoint war nicht sichtbar (Decorator vergessen)
- Date-Based Filtering war anfangs schwer nachzuvollziehen
- Datenbank-Beziehung zwischen Notes und Tags hat nicht funktioniert (kein klares Mapping)


---

#### 3. 💡 How did I overcome them?
- Path vs Query Parameters zuhause nochmal angeschaut
- Code aus der Präsi Schritt für Schritt nachvollzogen und selbst nachgebaut
- Fehlercodes gelesen und mit bestehendem Code verglichen, um Probleme zu finden
- bei Routing-Problem erkannt:
→ FastAPI arbeitet von oben nach unten
→ deshalb Reihenfolge der Endpoints entscheidend
- bei Tag-Fehler:
→ ChatGPT genutzt, um die Fehlermeldung zu verstehen
→ Problem erkannt (falsche Rückgabe von load_notes)
→ Code angepasst (notes_db entfernt)
- Filter-Probleme gelöst, indem ich:
→ überprüft habe, ob Daten beim Erstellen korrekt gespeichert werden
→ fehlende Felder ergänzt habe (z.B. tags)
- notes_db besser verstanden, dadurch gezielter eingesetzt bzw. entfernt, wo es Probleme gemacht hat
- Top Tags:
→ erst eigener Ansatz probiert → dann Hinweis aus Präsi genutzt
→ Counter importiert und durch Code auf Website gelernt anzuwenden
→ Als es dann nicht funktioniert hat durch Chat GPT gemerkt, dass man Ergebnis von most_common() in variable speichern muss
- Unique Count: von sum() auf len() gewechselt, weil nur Anzahl benötigt wird
- PATCH Problem: durch Kommilitonen erkannt, dass "@" vor app.patch in meinem Code fehlte
- Datenbank-Beziehung: mit Code von Kommilitonen abgeglichen → verstanden, dass eine Link-Tabelle nötig ist


---

## Week 2

### Day 4

#### 1. ✅ What did I accomplish?
- Einführung in automatisiertes Testen mit pytest und requests
- neue Dateien main_day4.py und test_day4.py im Unterricht erstellt
- grundlegende Teststruktur kennengelernt (Arrange – Act – Assert)
- erste einfache Tests für Beispiel-Endpunkte geschrieben und ausgeführt


Zuhause:
- Hausaufgabe gestartet und eigene test_notes.py für meine Notes API erstellt
- alle Endpunkte getestet
- Grenzfälle getestet
- gemerkt, dass mir ein Feature noch fehlt: Date-Based Filtering und dieses eingefügt

---

#### 2. 🚧 What challenges did I face?
- am Anfang hat pytest keine Tests erkannt, weil ich die Benennung nicht korrekt hatte
- Unsicherheit, wie Tests genau aufgebaut sein müssen und was sinnvoll geprüft werden sollte
- Schwierigkeit, realistische Error Cases zu definieren (z. B. welche IDs „nicht existieren“)
- teilweise schwer nachzuvollziehen, ob Fehler wirklich korrekt getestet werden oder nur zufällig funktionieren
- Unsicherheit, ob ich zu viel oder zu wenig teste
- Unsicherheit, welche Grenzfälle sinnvoll sind

---

#### 3. 💡 How did I overcome them?
- Problem mit „0 Tests gefunden“ gelöst, indem ich Dateinamen überprüft habe
- Teststruktur besser verstanden durch Beispiele aus der Präsentation → eigene Tests daran angelehnt aufgebaut
- Error Cases verbessert: zuerst mit festen IDs gearbeitet, danach auf allgemeinere Lösungen umgestellt (z. B. Schleifen mit negativen und großen IDs)
- Tests strukturiert: erst Normalfall testen, dann Grenzfall
- bei Unsicherheiten Fehler analysiert und ausprobiert
- ChatGPT genutzt, Tests für Grenzfälle erstellen zu lassen 


---

### Day 5

#### 1. ✅ What did I accomplish?
- Da ich krank war, habe ich Tag 5 zuhause mit der Präsentation nachgearbeitet
- Pydantic Validation genauer kennengelernt
- Field Constraints für NoteCreate und NoteUpdate eingebaut
- Validatoren für title, category und tags erstellt
- mehrere gültige und ungültige Requests in /docs getestet

---

#### 2. 🚧 What challenges did I face?
- Unterschied zwischen Field, field_validator und model_validator war zuerst etwas verwirrend
- Probleme mit Groß- und Kleinschreibung bei Kategorien
- Fehler durch unterschiedliche Field Imports von Pydantic und SQLModel

---

#### 3. 💡 How did I overcome them?
- Präsentation Schritt für Schritt durchgearbeitet
- Änderungen direkt im Code ausprobiert und über /docs getestet
- Regex-Problem gelöst, indem die Kategorie erst im Validator normalisiert wird (value = value.lower())
- beim Field-Import-Fehler ChatGPT zur Erklärung genutzt


---

### Day 6

#### 1. ✅ What did I accomplish?
- Da ich arbeiten musste und keine Aufnahme (zu diesem Zeitpunkt) gefunden habe, habe ich Day 6 selbstständig mit der Präsentation nachgearbeitet
- class_based_decorator.py erstellt
- icecream installiert und kurz angeschaut
- Test-Suite heruntergeladen und ausgeführt
- gelernt, wie man große Fehlermengen systematisch analysiert
- mehrere Probleme in meiner API gefunden und angepasst:
- Root Endpoint ergänzt
- Date Validation verbessert
- Statistik Endpoint angepasst
- verstanden, wie stark viele Tests und Features zusammenhängen
- gemerkt, wie viele Fehler zusammenhängen und auch verschwinden, wenn ein Problem gelöst wird

---

#### 2. 🚧 What challenges did I face?
- zuerst überfordert von der Menge an Fehlermeldungen
- Unsicherheit, ob ich die Tests oder meine API anpassen soll
- viele Fehler durch Validation-Regel mit dem work-Tag
- Probleme bei Date Filtering (created_after, created_before)
- Fehlercodes und Assertions teilweise schwer zu lesen
- allgemein: inzwischen schwer teilweise Code mit Kommilitonen abzugleichen, da viele nicht auf dem neusten Stand sind oder es nicht gut genug verstehen

---

#### 3. 💡 How did I overcome them?
- Fehler Schritt für Schritt analysiert
- Testnamen gelesen, Testcode verstehen, in main.py korrespondierenden Code gesucht und versucht zu verstehen, wo das Problem liegt
- bei work-Tag Fehler die Testdaten mit meiner Validation verglichen und den Validator auskommentiert
- created_after Problem im Code eingegrenzt und verstanden, dass datetime.fromisoformat() fehlschlägt
→ zuerst eigene Lösung  ausprobiert, nach Scheitern mit Hilfe von ChatGPT eine einfachere Lösung mit datetime | None = None umgesetzt und erklären lassen
- letzten Fehler gelöst, indem ich den Test genauer gelesen habe:
→ Test erwartet maximal 5 Top Tags
→ im Code waren aber Top 10 eingestellt
- Problem mit Kommilitonen abzugleichen: eigneständiges Arbeiten mit den Präsentationen

---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?
- mit Streamlit begonnen und erstes Frontend für die Notes API aufgebaut
- frontend.py angelegt
- Streamlit installiert und erste Tests durchgeführt
- Streamlit „Hello World“ Ausgabe getestet
- zusätzlichen Exploration-Ordner für kleine Tests und Experimente erstellt
- Streamlit Dokumentation angeschaut und begonnen damit zu arbeiten


Zuhause:
- Frontend aufgebaut
- Imports und grundlegende Struktur aus der Übung übernommen
- API URL eingebunden und an bisherigen FastAPI Code orientiert
- Vorgehen für das Frontend geplant:
→ Notes laden, Notes in Dropdown anzeigen, ausgewählte Note anzeigen, neue Notes erstellen können

Funktion 1 - Notes anzeigen:
- Funktion zum Laden der Notes gebaut
→ requests.get() verwendet
→ /notes Endpoint angesprochen
→ Error Handling ergänzt
- geprüft, ob die geladenen Notes korrekt zurückgegeben werden
- Dropdown-Menü mit st.selectbox() erstellt
→ dafür in der Streamlit Dokumentation nach Beispielen gesucht und diese auf meinen Use Case angepasst
- zuerst Liste mit Note-Titeln erstellt
- Schleife gebaut, um alle Titel aus den geladenen Notes herauszunehmen
- Auswahl der Note umgesetzt:
→ nach Auswahl werden Titel, Content, Tags, Category und Created at angezeigt
- Ausgabe zuerst mit st.write() umgesetzt
- verstanden, dass select_note den aktuell ausgewählten Wert der Selectbox speichert
- mehrere Notes mit gleichem Titel getestet
→ festgestellt, dass dadurch mehrere Notes gleichzeitig angezeigt werden
→ Lösung zuerst über zusätzlichen Vergleich mit Datum und Uhrzeit, dafür Titel und Datum gemeinsam angezeigt und abgeglichen
- Notes zusätzlich nach Erstelldatum sortiert
- Datumsausgabe gekürzt und schöner formatiert

Funktion 2 – Neue Notes erstellen:
- Eingabefelder für Titel, Content, Tags und Category erstellt
- text_input, text_area und selectbox getestet und angepasst
- Submit Button ergänzt
- Funktion geschrieben, die nach Klick auf den Button eine neue Note erstellt
- Tags als Liste verarbeitet
- Notizdaten als Dictionary aufgebaut und mit requests.post() an die API geschickt
- erreicht, dass neu erstellte Notes direkt in der Liste auftauchen
- Session State genutzt, damit Felder nach erfolgreichem Submit geleert werden
→ dafür Beispiele anderer Entwickler angeschaut und versucht nachzuvollziehen, wie session_state und dynamische Keys funktionieren
- Frontend mehrfach getestet und weiter angepasst


---

#### 2. 🚧 What challenges did I face?
- Probleme bei Notes mit gleichem Titel → mehrere Notes wurden gleichzeitig angezeigt bei Auswahl aus Liste
- unschöne Darstellung durch lange Datumswerte
- Schwierigkeiten wie bei Submit-Funktion Tags übergeben werden sollen → API erwartet Liste, Textfeld liefert aber String
- nach erstem Submit passierte zunächst nichts, später zwar Request abgeschickt, aber Error beim Erstellen der Note
- Content Feld mit normalem text_input war zu klein für längere Texte
- Probleme beim Zurücksetzen der Eingabefelder nach erfolgreichem Submit
- Sortierung der Notes funktionierte zunächst falsch → statt nach Datum wurde nach String-Inhalt sortiert
- Generell Unwissenheit über Streamlit und Coding dafür


#### 3. 💡 How did I overcome them?
- viel mit der Streamlit Dokumentation gearbeitet, Beispielcodes getestet und für mich angepasst
- Funktionen Schritt für Schritt aufgebaut und zwischendrin nachgedacht, statt alles gleichzeitig umzusetzen (hatte das erste mal so richtig das Gefühl, einen eigenen Flow fürs Funktionen schreiben zu haben, dank der Übungen der Vortage)
- einmal auch mit einem Kommilitonen ausgetauscht zum Aufbau des Frontends
- bei gleichen Titeln:
→ zusätzlichen Vergleich über mit Datum ergänzt
- Datumsdarstellung verbessert → Datum mit .split("T") gekürzt (Dafür ChatGPT gefragt und Code erklären lassen)
- Submit Tags Problem:
→ zunächst grundlegende Funktion selbst geschrieben (Bedingung wenn Button gedrückt wird, Endpointanbindung, note_data)
→ danach ChatGPT genutzt, um Code für Tags zu ergänzen
- Submit Problem gelöst → Code in Ruhe angeschaut und erkannt, dass Funktion zwar definiert, aber nie aufgerufen wurde
- Error beim Posten → Code angeschaut, nicht drauf gekommen, dann ChatGPT analysieren lassen und erkannt, dass ich meine Tags Variable versehentlich überschrieben hatte
- größeres Content Feld → Streamlit Dokumentation nach Alternativen durchsucht und text_area() gefunden
- Session State:
→ Gegoogelt, Code anderer Leute in Foren übernommen und angepasst
→ Denk- und Syntaxfehler mit Hilfe von ChatGPT verbessert
- Sortierung der Titel in der Liste:
→ zuerst note_titles.sort() ausprobiert
→ erkannt, dass dadurch nur Strings sortiert werden
→ Lösung: komplette Notes vorher schon sortieren
- Frontend immer wieder direkt getestet und angepasst, statt zu viel auf einmal zu programmieren

---

### Day 8

#### 1. ✅ What did I accomplish?
- Frontend optisch weiter verbessert
- Streamlit Dokumentation weiter genutzt und verschiedene UI Elemente ausprobiert
- Header, Titel und Divider eingebaut und angepasst
- gelernt, wie Streamlit Themes funktionieren
- Farben und Theme angepasst:
→ herausgefunden, dass die App-Farben über eine config.toml Datei gesteuert werden
→ .streamlit Ordner und Config-Datei angelegt
→ verschiedene Farbkombinationen ausprobiert
→ Streamlit Dokumentation parallel offen gehabt und Theme-Werte angepasst und festgestellt, dass manche Textfarben in Streamlit nicht einfach getrennt angepasst werden können
→ gelernt, dass dafür CSS nötig wäre
→ deshalb Design nur etwas angepasst statt CSS einzubauen


Darstellung der Notes verbessert:
- Titel als richtigen Titel dargestellt statt als "Titel: ..."
- Datum gekürzt und übersichtlicher gemacht
- Tags schöner formatiert
- Container für ausgewählte Notes eingebaut
-  Content übersichtlicher dargestellt
- gelernt, wie man Listen schöner anzeigen kann → join() genutzt, damit Tags nicht mehr als rohe Python-Liste angezeigt werden
- Problem mit gleichen Titeln endgültig sauber gelöst:
→ erkannt, dass die ID eigentlich die logischste Lösung ist
→ Notes intern über IDs unterschieden statt über Titel + Datum
→ Dropdown trotzdem nur mit Titeln angezeigt
- festgestellt, dass Zeilenumbrüche im Content verloren gehen
→ Ausgabe angepasst, damit Absätze erhalten bleiben
- .gitignore überprüft und mit GitHub Vorlagen verglichen


Projekt für Abgabe vorbereitet:
- uv run fastapi dev main.py getestet
- uv run pytest test_main.py getestet
- uv run streamlit run frontend.py getestet
→ funktioniert alles
- README geschrieben → dafür verschiedene GitHub README Beispiele angeschaut -> Grundstruktur geschrieben, ChatGPT Code Beispiele erstellen lassen und diese getestet
- Code aufgeräumt:
→ alte Kommentare entfernt
→ unnötigen alten Code gelöscht (z.B. Übungen, Code für json-version)
→ versucht alles einheitlicher und übersichtlicher zu strukturieren
→ Ordnerstruktur überprüft

---

#### 2. 🚧 What challenges did I face?
- Unsicherheit, wie weit man Streamlit optisch überhaupt anpassen kann
- Problem mit Theme:
→ nicht alle Farben separat anpassbar
→ insbesondere keine Secondary Text Color möglich
- Probleme bei der Darstellung der Notes-Liste:
→ nach Änderung der Datumsanzeige wurden plötzlich keine Notes mehr angezeigt
→ erneut Problem mit mehreren Notes gleichen Titels
- Challenge: lange Datumsstrings zu kürzen
- Darstellung der Tags in Streamlit ändern
- zunächst nicht verstanden, warum Absätze im Content verloren gehen


---

#### 3. 💡 How did I overcome them?
- viel ausprobiert und direkt in Streamlit getestet → Tipp mit dauerhaft rerun und zweiter Bildschirm war sehr hilfreich
- Streamlit Dokumentation genutzt, um passende UI Elemente zu finden und Code direkt auszuprobieren

bei Theme-Anpassung:
- gegooglet, wie man primaryColor und Themes verändert
- Streamlit Dokumentation genutzt
- dadurch auf .streamlit/config.toml gestoßen
- verschiedene Farben ausprobiert bis das Design stimmig wirkte
bei fehlender Secondary Text Color:
- herausgefunden, dass dafür CSS nötig wäre → entschieden, das Design stattdessen einfacher zu lassen

Tags schöner dargestellt:
- gegoogelt wie man Python-Listen schöner als Text ausgeben kann
- auf ", ".join(...) in Forum gestoßen und an meinen Code angepasst

Problem mit verschwundener Anzeige der Notes aus der Liste:
- Code Schritt für Schritt angeschaut
- erkannt, dass die if-Bedingung wegen verändertem Datum nicht mehr erfüllt wurde → Vergleich angepasst
- danach erneut Problem mit mehreren Notizen mit gleichen Titeln
- nachgedacht und erst dann realisiert, dass IDs eigentlich die eindeutigste Lösung sind
→ im Nachhinein gemerkt, dass ich mir vorher unnötig komplizierte Lösungen gebaut hatte
→ durch die Erfahrung der Vortage konnte ich die Umstellung auf IDs aber relativ schnell selbst umsetzen

Datum gekürzt:
- ChatGPT genutzt, um passende Lösung zu finden und erklären zu lassen

Absätze im Content:
- gegooglet → gelernt, dass st.text() Zeilenumbrüche besser übernimmt als st.write()

.gitignore:
- mit GitHub Vorlagen verglichen und zusätzlich ChatGPT gefragt, welche Einträge sinnvoll sind
- vor Abgabe alles nochmal systematisch getestet


---


# 🎉 Yay, I did it! 🎓✨













