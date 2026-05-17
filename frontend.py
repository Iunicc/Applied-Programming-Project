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

########################################
# INTERFACE
########################################
# App Title
st.title("_My_ :primary[Notes]")


#--------------------------------
# Notes List
#--------------------------------
# Header View Notes
st.header("View Notes", divider="yellow")

notes = load_notes()
notes.sort(key=lambda note: note["created_at"], reverse=True)

note_ids = []

for note in notes:
    note_ids.append(note["id"])

select_note_id = st.selectbox(
    "All Notes",
    note_ids,
    format_func=lambda note_id: next(
        note["title"] for note in notes if note["id"] == note_id
    ),
    index=None,
    placeholder="Select Note",
)
for note in notes:
    if note["id"] == select_note_id:
        date = note["created_at"].split("T")[0]

        with st.container(border=True):
            st.subheader(note["title"])
            st.text(note["content"])
            st.caption(f"ID: {note["id"]}")
            st.caption("Tags: " + ", ".join(note["tags"]))
            st.caption(f"Category: {note["category"]}")
            st.caption(f"Created at: {date}")
        

#--------------------------------
# Write Notes
#--------------------------------
# Header Write New Notes
st.header("Write new Note", divider="yellow")

# Text Input
title = st.text_input("Title", key=f"title_input_{st.session_state['form_key']}")
content = st.text_area("Content", key=f"content_input_{st.session_state['form_key']}")
tags = st.text_input(
    "Tags",
    placeholder="e.g. urgent, project, test",
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

        note_data = {
        "title": title,
        "content": content,
        "category": category,
        "tags": tags_list
        }

        response = requests.post(f"{URL}/notes", json=note_data)
        if response.status_code == 201:
            st.session_state["form_key"] += 1
            st.rerun()
                    
if submitted:
    post_note()
   


