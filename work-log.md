# Work Log

**Student Name:** 

Instructions: Fill out one log for each course day. Content to consider: Course Sessions + Assignment

## Template:

---

## 1. ✅ What did I accomplish?

_Reflect on the activities, exercises, and work you completed today._

**Guiding questions:**
- What topics or concepts did you work with?
- What exercises or projects did you complete?
- What tools or technologies did you use?
- What did you learn or practice?

---

## 2. 🚧 What challenges did I face?

_Describe any difficulties, obstacles, or confusing moments you encountered._

**Guiding questions:**
- What was difficult to understand?
- Where did you get stuck?
- What errors or problems did you face?
- What felt frustrating or confusing?

---

## 3. 💡 How did I overcome them?

_Explain how you overcame the challenges or what help you needed._

**Guiding questions:**
- What strategies did you try?
- Who or what helped you (instructor, classmates, documentation)?
- What did you learn from solving the problem?
- What questions do you still have?


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
- gesamten bisherigen Code nochmal in Ruhe durchgegangen und besser verstanden, wie eine API aufgebaut ist
verstanden, dass für jeden URL-Pfad ein eigener Endpoint definiert werden muss
- Filter-Logik im Code nachvollzogen:
→ mit if-Bedingungen wird geprüft, ob eine Note die Bedingungen erfüllt
→ wenn nicht, wird sie übersprungen (continue)
→ wenn ja, wird sie in die Ergebnisliste aufgenommen
- Unterschied zwischen Path und Query Parameters klar verstanden:
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
- Link-Tabelle (NoteTagLink) eingeführt
- Verknüpfung zwischen Note und Tag hergestellt
- getestet, ob Tags korrekt gespeichert und geladen werden
- regelmäßig in /docs und über URL-Parameter getestet


---

#### 2. 🚧 What challenges did I face?
- Path vs Query Parameters im Unterricht zunächst nicht vollständig verstanden
- automatisiertes Testen (api_test) im Unterricht nicht gut mitbekommen
- Fehler bei eigenen Endpoints (z. B. Syntaxfehler wie fehlende : oder {})
- unerwartetes Verhalten bei /test/123 wegen falscher Endpoint-Reihenfolge
- Internal Server Error beim Arbeiten mit Tags
- Filter mit Tags und kombinierte Filter haben zunächst keine Ergebnisse geliefert
- Probleme mit notes_db (nicht definiert / falsche Verwendung)
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
→ fehlende Felder ergänzt (z.B. tags)
- notes_db besser verstanden, dadurch gezielter eingesetzt bzw. entfernt, wo es Probleme gemacht hat
- Top Tags:
→ erst eigener Ansatz probiert → dann Hinweis aus Präsi genutzt
→ Counter importiert und durch Code auf Website gelernt anzuwenden
→ Als es dann nicht funktoniert hat durch Chat GPT gemerkt, dass man Ergebnis von most_common() in variable speichern muss
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






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 6

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

## Week 3

### Day 7

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 8

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---

### Day 9

#### 1. ✅ What did I accomplish?






---

#### 2. 🚧 What challenges did I face?






---

#### 3. 💡 How did I overcome them?






---


# 🎉 Congratulations! You did it! 🎓✨













