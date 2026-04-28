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

class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

#--------------------------------
# Storage
#--------------------------------
NOTES_FILE = Path("data/notes.json")

def load_notes():
    """Load notes from JSON file and return notes list and next ID counter"""
    notes_db = []
    note_id_counter = 1

    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            data = json.load(f)
            notes_db = [Note(**note) for note in data]

            # Set counter to max ID + 1
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1

    return notes_db, note_id_counter


def save_notes(notes_db):
    """Save notes to JSON file after each change"""
    # Ensure data directory exists
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(NOTES_FILE, 'w') as f:
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)



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
            notes_db = [Note(**note) for note in data]
            
            # Set counter to max ID + 1
            if notes_db:
                note_id_counter = max(note.id for note in notes_db) + 1

#Save Notes to File
def save_notes():
    """Save notes to JSON file"""
    with open(NOTES_FILE, 'w') as f:
        # Convert Note objects to dicts
        notes_data = [note.dict() for note in notes_db]
        json.dump(notes_data, f, indent=2)

#--------------------------------
#App
#--------------------------------
#Create FastAPI App
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
#Create POST /notes Endpoint
@app.post("/notes", status_code=201)    # POST method, return 201
def create_note(note: NoteCreate):      # Function takes NoteCreate model
    """Create a new note"""             
    global note_id_counter              # Access global counter
    
    new_note = Note(                    # Create Note with ID
        id=note_id_counter,
        title=note.title,
        content=note.content,
        created_at=datetime.now().isoformat()
    )
    
    notes_db.append(new_note)           # Add to storage
    note_id_counter += 1                # Increment counter
    
    save_notes()

    return new_note                     # Return created note

#Create GET /notes Endpoint
@app.get("/notes")
def list_notes():
    """Get all notes"""
    return notes_db

#Create GET /notes/{note_id}
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