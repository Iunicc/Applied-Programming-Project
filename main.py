#--------------------------------
# Imports
#--------------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
datetime.now(timezone.utc).isoformat()
import json
from pathlib import Path

########################################
# First Exercise (Day 1)
########################################

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


########################################
# Note API Endpoints (Day 2)
########################################

#--------------------------------
# Data Models
#--------------------------------
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str           # <- Homework Day 2

class Note(BaseModel):
    id: int
    title: str
    content: str
    category: str           # <- Homework Day 2  
    created_at: str


#--------------------------------
# Storage
#--------------------------------
NOTES_FILE = Path("data/notes.json")
notes_db = []
note_id_counter = 1


#--------------------------------
#File Functions
#--------------------------------
#Load Notes from File
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

#Save Notes to File
def save_notes():
    """Save notes to JSON file"""
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, 'w') as f:
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)

#--------------------------------
# App
#--------------------------------
# Create FastAPI App
app = FastAPI(
    title="Note Taking API",
    description="Simple note management",
    version="1.0.0"
)

# Load existing notes when server starts
load_notes()

#--------------------------------
#Endpoints
#--------------------------------
# Create POST /notes Endpoint
@app.post("/notes", status_code=201)    # POST method, return 201
def create_note(note: NoteCreate):      # Function takes NoteCreate model
    """Create a new note"""             
    global note_id_counter              # Access global counter
    
    new_note = Note(                    # Create Note with ID
        id=note_id_counter,
        title=note.title,
        content=note.content,
        category=note.category,         # <- Homework Day 2
        created_at=datetime.now().isoformat()
    )
    
    notes_db.append(new_note)           # Add to storage
    note_id_counter += 1                # Increment counter
    
    save_notes()

    return new_note                     # Return created note

# Create GET /notes Endpoint
@app.get("/notes")
def list_notes():
    """Get all notes"""
    return notes_db

# Add Statistic Endpoint
@app.get("/notes/stats")
def get_notes_stats():
    """Get statistics about notes"""
    
    # Count by category
    categories = {}
    for note in notes_db:
        if note.category in categories:
            categories[note.category] += 1
        else:
            categories[note.category] = 1
    
    return {
        "total_notes": len(notes_db),
        "by_category": categories
    }

# Filter Notes by Category
@app.get("/notes/category/{category}")
def get_notes_by_category(category: str):
    """Get all notes in a specific category"""
    filtered_notes = []
    
    for note in notes_db:
        if note.category == category:
            filtered_notes.append(note)
    
    return filtered_notes

# Create GET /notes/{note_id}
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

# Add Delete Endpoint
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Delete a note by ID"""
    for i, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(i)
            save_notes()
            return {"message": "Note deleted"}
    
    raise HTTPException(404, "Note not found")
