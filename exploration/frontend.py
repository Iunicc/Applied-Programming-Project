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