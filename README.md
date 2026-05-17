# MyNotes App

A simple note taking app built with FastAPI, SQLModel, SQLite and Streamlit.

The application allows users to create, view, filter, update and delete notes. Each note contains a title, content, category, tags and a creation date. The backend provides a REST API while the frontend offers a simple graphical interface built with Streamlit.

The goal of the project was to combine backend development with a simple frontend and database integration in one application.

---

## Features

- Create new notes
- View all notes
- Display selected notes in the frontend
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

## System Requirements

The project was developed and tested with:

- Python 3.13
- uv
- FastAPI
- Streamlit
- SQLite

Required Python packages:

```bash
fastapi
sqlmodel
streamlit
requests
pytest
```

---

## Project Structure

```text
.
├── .streamlit/
│   └── config.toml
├── main.py
├── frontend.py
├── README.md
├── pyproject.toml
├── uv.lock
└── notes.db
```

### Important Files

- `main.py` → FastAPI backend and database logic
- `frontend.py` → Streamlit frontend
- `test_main.py` → automated tests
- `work-log.md` → documentation of the development process
- `notes.db` → SQLite database file

---

# Setup

Install all dependencies with uv:

```bash
uv sync
```

If dependencies are missing, install them manually:

```bash
uv add fastapi sqlmodel streamlit requests pytest
```

---

## Start the FastAPI Backend

Run:

```bash
uv run fastapi dev main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

The documentation can be used to test endpoints directly in the browser.

---

# Start the Streamlit Frontend

Open a second terminal and run:

```bash
uv run streamlit run frontend.py
```

The frontend will automatically open in the browser.

Default frontend URL:

```text
http://localhost:8501
```
The Streamlit frontend can:

load notes from the FastAPI backend
display notes inside a dropdown menu
show all note details
create new notes
sort notes by creation date
The frontend communicates with the backend using:

```python
URL = "http://127.0.0.1:8000"
```

---

# API Overview

## Root

```http
GET /
```

Returns basic API information.

---

## Notes

```http
GET /notes
POST /notes
GET /notes/{note_id}
PUT /notes/{note_id}
PATCH /notes/{note_id}
DELETE /notes/{note_id}
```

### Available Filters

The `/notes` endpoint supports query filters:

```text
category
search
tag
created_after
created_before
```

Example:

```text
http://127.0.0.1:8000/notes?category=school
```

---

## Tags

```http
GET /tags
GET /tags/{tag_name}/notes
```

---

## Categories

```http
GET /categories
GET /categories/{category_name}/notes
```

---

## Statistics

```http
GET /notes/stats
```

Returns:

- total number of notes
- notes per category
- most used tags

---

## Example: Create a Note with Python

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

Expected status code:

```text
201
```

---

## Example: Get All Notes with Python

```python
import requests

URL = "http://127.0.0.1:8000/notes"

response = requests.get(URL)

print(response.status_code)
print(response.json())
```

Expected status code:

```text
200
```

---

# Manual API Testing

The API can also be tested manually inside Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Then:

1. Open the endpoint
2. Click "Try it out"
3. Enter JSON data
4. Click "Execute"

Example JSON:

```json
{
  "title": "Design Idea",
  "content": "Portable modular workspace",
  "category": "ideas",
  "tags": ["design", "project"]
}
```

---

# Data Validation

The API validates incoming data with Pydantic and SQLModel.

Allowed categories:

```text
work
personal
school
ideas
general
```

Validation rules include:

- title must have at least 3 characters
- content must not be empty
- category must match an allowed category
- tags must contain at least 2 characters
- duplicate tags are automatically removed

The database tables are automatically created when the backend starts.

---

# Notes

The backend must be running before the frontend can load or create notes.

If the database should be reset completely, simply delete:

```text
notes.db
```

A new database file will automatically be created when the backend starts again.
