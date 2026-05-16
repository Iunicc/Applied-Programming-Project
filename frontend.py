'''
- Streamlit intsallieren
- Streamlit App "Hello, World!" erstellen und testen
- "Say no" - App als erster Test erstellen
    - API Documentation: https://github.com/hotheadhacker/no-as-a-service
    - API Endpoint: https://naas.isalman.dev/no
    - Button in Streamlit, der bei Klick eine Anfrage an den API Endpoint sendet und die Antwort anzeigt

- TO DOs Nachmittag:
    - Streamlit App mit 2 Funktionen von Notizen API
    - Funktion 1: Alle Notizen anzeigen
        - Liste von Titeln von Notizen anzeigen
        - Möglichkeit zu einem Titel den Inhalt, Tags, Category, etc. anzuzeigen
    - Funktion 2: Neue Notiz erstellen (Formular mit Titel und Inhalt, Button)
        - Erstellen einer neuen Notiz (Titel, Inhalt, Tags, Category)
        - Neu erstellte Notiz soll in Liste auftauchen

'''

#{"reason":"My broomstick is in the shop (you know how unreliable those are)."}

import streamlit as st
import requests

URL = "https://naas.isalman.dev/no"

response = requests.get(URL)

#st.write("Hello, World!")


def request_no():
    response = requests.get(URL)
    response_json = response.json()
    return response_json["reason"]

# Initialization
if 'text1' not in st.session_state:
    st.session_state['text1'] = request_no()
    print("init Text1")

if 'text' not in st.session_state:
    st.session_state['text'] = request_no()
    print("init Text")


name = st.text_input('Name', placeholder="Hier Name eingeben...")
st.write(name)


if st.button("Neuer Text1"):
    st.session_state['text1'] = request_no()

st.write(st.session_state["text1"])


if st.button("Neuer Text"):
    st.session_state['text'] = request_no()

st.write(st.session_state["text"])


with st.expander('session state'):
    st.write(st.session_state)

#------------------------------------------
# Day 7: Frontend

########################################
# IMPORTS
########################################
import streamlit as st
import requests


########################################
# URL
########################################
URL = "http://127.0.0.1:8000"

########################################
# FUNCTIONS
########################################
#--------------------------------
# Load Notes
#--------------------------------
def load_notes():
    response = requests.get(f"{URL}/notes")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Notes could not be loaded")
        return []  


#--------------------------------
# Notes List
#--------------------------------
notes = load_notes()
#st.write(notes)

note_titles = []

for note in notes:
    note_titles.append(note["title"] + " " + note["created_at"])


select_note = st.selectbox(
    "All Notes",
    (note_titles),
    index=None,
    placeholder="Select Note",
)

for note in notes:
    if (note["title"] + " " + note["created_at"] == select_note):
        st.write("Titel:", note["title"])
        st.write("ID:", note["id"])
        st.write("Content:", note["content"])
        st.write("Category:", note["category"])
        st.write("Tags:", note["tags"])
        st.write("Created at:", note["created_at"])

#st.write("You selected:", select_note)

#--------------------------------
# Write Notes
#--------------------------------
# Text Input
title = st.text_input("Title")
content = st.text_input("Content")
tags = st.text_input("Tags", placeholder="Type it like this: urgent, project, test")
category = st.selectbox("Category",
    ("work", "personal", "school", "ideas", "general"),
    index=None,
    placeholder="Select Category",
)

# Submit Button
submitted = st.button("Submit Note", type="primary")

def post_note():
    if submitted:
        tags_list = []

        if tags:
            for tag in tags.split(","):
                tags_list.append(tag.strip())

        # Daten übergeben
        note_data = {
        "title": title,
        "content": content,
        "category": category,
        "tags": tags_list
        }

        # Notiz posten
        response = requests.post(f"{URL}/notes", json=note_data)
        if response.status_code == 201:
            return response.json()
        else:
            st.error("Note could not be submitted")
            return [] 
        
if submitted:
    post_note()