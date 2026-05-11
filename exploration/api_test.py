import requests

URL = "http://127.0.0.1:8000"

def test_get_notes():
    response = requests.get(URL + "/notes")
    if response.status_code == 200:
        print("GET /notes - SUCCESS")
        print(response.json())
    else:
        print("GET /notes - FAILED")


def test_post_note():
    payload = {
        "title": "Test Note",
        "content": "Das ist ein Test",
        "category": "test",
        "tags": ["urgent", "demo"]
    }

    response = requests.post(URL + "/notes", json=payload)

    if response.status_code == 201:
        print("POST /notes - SUCCESS")
        print(response.json())
    else:
        print("POST /notes - FAILED")
        print(response.text)


if __name__ == "__main__":
    test_get_notes()
    test_post_note()
    
