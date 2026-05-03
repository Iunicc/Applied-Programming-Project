########################################
# IMPORTS
########################################
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
datetime.now(timezone.utc).isoformat()
import json
from pathlib import Path
from collections import Counter             # <- Homework Day 3
from typing import Optional                 # <- Homework Day 3

########################################
# DATA MODELS
########################################
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str           # <- Homework Day 2
    tags: list[str] = []    # <- Day 3

class Note(BaseModel):
    id: int
    title: str
    content: str
    category: str           # <- Homework Day 2  
    tags: list[str] = []    # <- Day 3
    created_at: str

class NoteUpdate(BaseModel):            # <- Homework Day 3
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None

########################################
# STORAGE
########################################
NOTES_FILE = Path("data/notes.json")
notes_db = []
note_id_counter = 1


########################################
# FILE FUNCTIONS
########################################
#--------------------------------
# Load notes from file
#--------------------------------
def load_notes():
    """Load notes from JSON file"""
    global notes_db, note_id_counter
    
    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            notes_db = [
                Note(**{**note, "category": note.get("category", "default")})
                for note in data
            ]
            
            # Set counter to max ID + 1
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1

#--------------------------------
# Save notes from file
#--------------------------------
def save_notes():
    """Save notes to JSON file"""
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, 'w') as f:
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)


########################################
# APP
########################################
# Create FastAPI App
app = FastAPI(
    title="Note Taking API",
    description="Simple note management",
    version="1.0.0"
)

# Load existing notes when server starts
load_notes()


########################################
# ENDPOINTS
########################################
# Reihenfolge wichtig
# /tests /courses -> Plural

#--------------------------------
# Create: POST -> Create Note
#--------------------------------
@app.post("/notes", status_code=201)    # POST method, return 201
def create_note(note: NoteCreate):      # Function takes NoteCreate model
    """Create a new note"""             
    global note_id_counter              # Access global counter
    
    new_note = Note(                    # Create Note with ID
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,         # <- Homework Day 2
        tags=note.tags,                 # <- Day 3
        created_at=datetime.now().isoformat()
    )
    
    notes_db.append(new_note)           # Add to storage
    note_id_counter += 1                # Increment counter
    
    save_notes()

    return new_note                     # Return created note


#--------------------------------
# Read: GET -> Read Notes
#--------------------------------
"""
List notes with optional filters
    
- category: Filter by category
- search: Search in title and content
- tag: Filter by tag
"""
@app.get("/notes")
def list_notes(
    category: str = None,
    search: str = None,
    tag: str = None,
    created_after: str = None,      # <- Homework Day 3
    created_before: str = None      # <- Homework Day 3
) -> list[Note]:
   
    load_notes()
    
    # Apply filters
    filtered = []
    for note in notes_db:
        # Filter by category
        if category and note.category != category:
            continue
        
        # Filter by search term
        if search:
            search_lower = search.lower()
            title_match = search_lower in note.title.lower()
            content_match = search_lower in note.content.lower()
            if not (title_match or content_match):
                continue
        
        # Filter by tag
        if tag and tag not in note.tags:
            continue
        
        # Homework Day 3
        # Filter by date
        if created_after and note.created_at < created_after:
            continue

        if created_before and note.created_at > created_before:
            continue

        filtered.append(note)
    
    return filtered

#--------------------------------
# Read: GET -> Get Stats about Notes
#--------------------------------
@app.get("/notes/stats")
def get_notes_stats():
    load_notes()

    # Count by category
    categories = {}
    for note in notes_db:
        if note.category in categories:
            categories[note.category] += 1
        else:
            categories[note.category] = 1

    # Top Tags: Count tags, then fnd most common (Counter objects)
    # Homework Day 3
    tags_count = Counter()
    for note in notes_db:
        for word in note.tags:
            tags_count[word] += 1
    top_tags = tags_count.most_common(10)

    # Unique tags count: Count tags only once, then addition
    # Homework Day 3
    unique = {}
    for note in notes_db:
        for word in note.tags:
            if word not in unique:
                unique[word] = 1        
    unique_tags_count = len(unique)

    return {
        "total_notes": len(notes_db),
        "by_categoriy": categories,
        "top_tags": top_tags,
        "unique_tags_count": unique_tags_count
    }


#--------------------------------
# Read: GET -> Get Notes by ID
#--------------------------------
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Get a specific note by ID"""
    for note in notes_db:
        if note.id == note_id:
            return note
    
    # Not found - raise 404 error
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


#--------------------------------
# Read: GET -> Get Notes by Category
#--------------------------------
@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):
    """Get all notes in a specific category"""
    filtered_notes = []
    
    for note in notes_db:
        if note.category == category:
            filtered_notes.append(note)
    
    return filtered_notes


#--------------------------------
# Read: GET -> Get all exisitng Tags
#--------------------------------
# Get all existing Tags
@app.get("/tags")
def list_tags() -> list[str]:
    """Get all unique tags from all notes"""
    
    load_notes()
    
    # Collect all tags
    all_tags = set()
    for note in notes_db:
        for tag in note.tags:
            all_tags.add(tag)
    
    # Return sorted list
    return sorted(list(all_tags))


#--------------------------------
# Read: GET -> Get Notes by Tags
#--------------------------------
@app.get("/tags/{tag_name}/notes")
def get_notes_by_tag(tag_name: str) -> list[Note]:
    """Get all notes with a specific tag"""
    
    load_notes()
    
    # Filter notes by tag
    filtered = []
    for note in notes_db:
        if tag_name in note.tags:
            filtered.append(note)
    
    return filtered

#--------------------------------
# Read: GET -> Get all unique categories
#--------------------------------
# Homework Day 3
@app.get("/categories")
def list_categories() -> list[str]:
    load_notes()

    unique_categories = {}
    for note in notes_db:
        if note.category not in unique_categories:
            unique_categories[note.category] = 1

    # Collect unique categories
    categories_list = []
    for category in unique_categories:
        categories_list.append(category)

    # Return sorted list
    return sorted(categories_list)


#--------------------------------
# Read: GET -> Get all Notes in category
#--------------------------------
# Homework Day 3
@app.get("/categories/{category_name}/notes")
def get_notes_by_category(category_name: str) -> list[Note]:
    load_notes()

    # Filter notes by category
    filtered_notes = []
    for note in notes_db:
        if note.category == category_name:
            filtered_notes.append(note)
    
    return filtered_notes


#--------------------------------
# Update: PUT -> Updating existing Note
#--------------------------------
@app.put("/notes/{note_id}")
def update_note(note_id: int, note_update: NoteCreate) -> Note:
    """Update an existing note"""
    
    load_notes()
    
    # Find the note
    for i, note in enumerate(notes_db):
        if note.id == note_id:                  # Keep original ID
            # Update note (keep id and created_at)
            updated_note = Note(
                id=note.id,
                title=note_update.title,        # New title
                content=note_update.content,
                category=note_update.category,
                tags=note_update.tags,
                created_at=note.created_at      # Keep original timestamp
            )
            
            notes_db[i] = updated_note
            save_notes()
            return updated_note
    
    # Not found
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )

#--------------------------------
# Update: PATCH -> Partially update Note
#--------------------------------
# Homework Day 3
@app.patch("/notes/{note_id}")
def partial_update_note(note_id: int, note_update: NoteUpdate) -> Note:
    """
    Partially update a note (only provided fields)
    Unlike PUT, PATCH only updates fields you provide
    """
    load_notes()

    for i, note in enumerate(notes_db):
        if note.id == note_id:
            # Update only provided fields (Homework Day 3)
            if note_update.title is not None:
                note.title = note_update.title

            if note_update.content is not None:
                note.content = note_update.content

            if note_update.category is not None:
                note.category = note_update.category

            if note_update.tags is not None:
                note.tags = note_update.tags

            notes_db[i] = note
            save_notes(notes_db)
            return note
    
    raise HTTPException(status_code=404, detail="Note not found")


#--------------------------------
# Delete: DELETE -> Delete Note
#--------------------------------
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Delete a note by ID"""
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(i)
            save_notes()
            return {"message": "Note deleted"}
    
    raise HTTPException(404, "Note not found")


########################################
# ÜBUNGEN
########################################
#--------------------------------
# Hello World + Hausaufgabe (Day 1)
#--------------------------------
'''
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

#@=Decorator /name (name)=kann eigenen namen angeben, wenn name angegeben wird läuft Funktion darunter durch
@app.get("/name/{name}")
def greet_name(name: str):
    return {"message": f"Hello,{name}!"} #IP/name/Manuel -> Ausgabe im Browser

#Aufgabe: Weiteren Endpunkt bauen:
@app.get("/zahl/{zahl}")
def add_one(zahl: int):
    return {zahl +1}
'''

#--------------------------------
# Path & Query Parameters (Day 3)
#--------------------------------
# Path: Bestimmter vorgegebener Pfad z.B. /notes/note_id
# Query Parameters: Resultate filtern oder modifizieren z.B. /notes?note_id=1
 
@app.get("/queryparameters")
def query_parameters(param1: str = None, param2: int = None) -> dict:
    namen = ['martin', 'sophia', 'michael', 'emma', 'maria', 'mathias', 'johannes', 'laura', 'mara']
    if not param1:
        return{"namen": namen}
    
    namen_gefiltert = []
    for name in namen:
        if param1 is None or param1 in name:
            namen_gefiltert.append(name)

    return {
        "param1": param1,
        "param2": param2,
        "namen": namen_gefiltert
    }

#Note anlegen endpunkt ändern -> in Datenbank schreiben und rauslesen

#---------------------------------
# Path Parameters (Day 3)
#---------------------------------
# Practice Endpoint Order
@app.get("/test/123")
def test_fixed():
    return {
        "fixed message": "Hallo 123"
        }

@app.get("/test/{value}")
def test_value(value: str):
    return {
        "value": value
    }

@app.get("/test/{value}/test2/{value2}")
def test_test2_value(value: str, value2: str):
    return {
        "value": value,
        "value2": value2
    }