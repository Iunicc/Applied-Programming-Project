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
# Session State
#--------------------------------
if "form_key" not in st.session_state:
    st.session_state["form_key"] = 0

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
st.title("_My_ :primary[Notes]")
st.header("View Notes", divider="yellow")

notes = load_notes()
notes.sort(key=lambda note: note["created_at"], reverse=True)

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

#--------------------------------
# Write Notes
#--------------------------------
st.header("Write new Note", divider="yellow")

# Text Input
title = st.text_input("Title", key=f"title_input_{st.session_state['form_key']}")
content = st.text_area("Content", key=f"content_input_{st.session_state['form_key']}")
tags = st.text_input(
    "Tags",
    placeholder="Type it like this: urgent, project, test",
    key=f"tags_input_{st.session_state['form_key']}"
)
category = st.selectbox(
    "Category",
    ("work", "personal", "school", "ideas", "general"),
    index=None,
    placeholder="Select Category",
    key=f"category_input_{st.session_state['form_key']}"
)

# Submit Button
submitted = st.button("Submit Note", type="primary", width="stretch")

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
            st.session_state["form_key"] += 1
            st.rerun()
                    
if submitted:
    post_note()
   


