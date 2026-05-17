# My Notes App

A simple note taking app built with FastAPI, SQLModel, SQLite and Streamlit.

The app allows users to create, view, update, filter and delete notes. Each note has a title, content, id, category, tags and a creation date. The backend provides a REST API and the frontend provides a simple Streamlit interface.

---

## Features

- Create new notes
- View all notes
- View one selected note in the frontend
- Filter notes by category, search term, tag and date
- Update notes with PUT
- Partially update notes with PATCH
- Delete notes
- View all tags
- View notes by tag
- View all categories
- View notes by category
- View basic note statistics

---

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Streamlit
- pytest
- uv

---

## Project Structure

```text
.
├── .streamlit/
│   └── config.toml
├── main.py
├── frontend.py
├── work-log.md
├── README.md
├── pyproject.toml
├── uv.lock
└── notes.db
```

---

# Setup

```bash
uv sync
```

```bash
uv add fastapi sqlmodel streamlit requests pytest
```

---

## Start the FastAPI Backend

```bash
uv run fastapi dev main.py
```

```text
http://127.0.0.1:8000
```

```text
http://127.0.0.1:8000/docs
```

---

## Start the Streamlit Frontend

```bash
uv run streamlit run frontend.py
```

---

# API Overview

## Root

```http
GET /
```

## Notes

```http
GET /notes
POST /notes
GET /notes/{note_id}
PUT /notes/{note_id}
PATCH /notes/{note_id}
DELETE /notes/{note_id}
```

## Tags

```http
GET /tags
GET /tags/{tag_name}/notes
```

## Categories

```http
GET /categories
GET /categories/{category_name}/notes
```

## Statistics

```http
GET /notes/stats
```

---

# Example: Create a Note with Python

```python
import requests

URL = "http://127.0.0.1:8000/notes"

note_data = {
    "title": "Homework",
    "content": "Finish the README file",
    "category": "school",
    "tags": ["homework", "project"]
}

response = requests.post(URL, json=note_data)

print(response.status_code)
print(response.json())
```

---

# Example: Get All Notes with Python

```python
import requests

url = "http://127.0.0.1:8000/notes"

response = requests.get(url)

print(response.status_code)
print(response.json())
```

---

# Example: Filter Notes

## Filter by category

```text
http://127.0.0.1:8000/notes?category=school
```

## Filter by tag

```text
http://127.0.0.1:8000/notes?tag=project
```

## Search in title and content

```text
http://127.0.0.1:8000/notes?search=readme
```

## Filter by date

```text
http://127.0.0.1:8000/notes?created_after=2026-05-01
```

---

# Data Validation

Allowed categories:

```text
work
personal
school
ideas
general
```

Validation rules:
- title must have at least 3 characters
- content must not be empty
- category must be one of the allowed categories
- tags must have at least 2 characters
- duplicate tags are removed

---

# Frontend

The frontend communicates with:

```python
URL = "http://127.0.0.1:8000"
```

---

# Notes

The backend must be running before the frontend can load or create notes.
