########################################
# IMPORTS
########################################
import requests
import pytest
from faker import Faker

########################################
# URL
########################################
BASE_URL = "http://127.0.0.1:8000"



########################################
# TESTS
########################################
# -----------------------------------------------------
# POST /notes
# -----------------------------------------------------
def test_create_note():
    note_data = {
        "title": "Test Note",
        "content": "Das ist ein Test",
        "category": "Testing",
        "tags": ["test", "pytest"]
    }

    response = requests.post(f"{BASE_URL}/notes", json=note_data)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "Das ist ein Test"
    assert data["category"] == "Testing"
    assert "id" in data
    assert "created_at" in data

# -----------------------------------------------------
# GET /notes
# -----------------------------------------------------
def test_list_notes():
    response = requests.get(f"{BASE_URL}/notes")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)


def test_update_nonexistent_note():
    updated_data = {
        "title": "Updated",
        "content": "Updated",
        "category": "Test",
        "tags": []
    }

    for note_id in range(-10, 0):
        response = requests.put(f"{BASE_URL}/notes/{note_id}", json=updated_data)

        assert note_id < 0
        assert response.status_code == 404

    for note_id in range(100000, 100010):
        response = requests.put(f"{BASE_URL}/notes/{note_id}", json=updated_data)

        assert note_id >= 100000
        assert response.status_code == 404

# -----------------------------------------------------
# GET /notes/{id}
# -----------------------------------------------------
def test_get_note_by_id():
    note_data = {
        "title": "Note für ID Test",
        "content": "Diese Note wird danach per ID gesucht",
        "category": "Testing",
        "tags": ["id-test"]
    }

    create_response = requests.post(f"{BASE_URL}/notes", json=note_data)

    assert create_response.status_code == 201

    created_note = create_response.json()
    note_id = created_note["id"]

    response = requests.get(f"{BASE_URL}/notes/{note_id}")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == note_id
    assert data["title"] == "Note für ID Test"
    assert data["content"] == "Diese Note wird danach per ID gesucht"
    assert data["category"] == "Testing"

    
# -----------------------------------------------------
# PUT /notes/{id}
# -----------------------------------------------------
def test_update_note():
    
    note_data = {
        "title": "Original",
        "content": "Original Content",
        "category": "Test",
        "tags": ["old"]
    }

    create_response = requests.post(f"{BASE_URL}/notes", json=note_data)
    note_id = create_response.json()["id"]

    
    updated_data = {
        "title": "Updated Title",
        "content": "Updated Content",
        "category": "Updated",
        "tags": ["new"]
    }

    response = requests.put(f"{BASE_URL}/notes/{note_id}", json=updated_data)

    
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated Content"
    assert data["category"] == "Updated"
    assert data["tags"] == ["new"]

# ID 999999 nonexistend
'''
def test_get_nonexistent_note():
    response = requests.get(f"{BASE_URL}/notes/999999")

    assert response.status_code == 404

    data = response.json()
    assert data["detail"] == "Note not found"
'''
# ID nonexistend
def test_get_nonexistent_note():
    for note_id in range(-10, 0):
        response = requests.get(f"{BASE_URL}/notes/{note_id}")

        assert note_id < 0
        assert response.status_code == 404

    for note_id in range(100000, 100010):
        response = requests.get(f"{BASE_URL}/notes/{note_id}")

        assert note_id >= 100000
        assert response.status_code == 404

# -----------------------------------------------------
# DELETE
# -----------------------------------------------------
def test_delete_note():
    note_data = {
        "title": "Delete Test",
        "content": "Diese Note wird gelöscht",
        "category": "Testing",
        "tags": ["delete"]
    }

    create_response = requests.post(f"{BASE_URL}/notes", json=note_data)
    assert create_response.status_code == 201

    note_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/notes/{note_id}")

    assert delete_response.status_code == 204

    get_response = requests.get(f"{BASE_URL}/notes/{note_id}")

    assert get_response.status_code == 404

# ID nonexistend
def test_delete_nonexistent_note():
    for note_id in range(-10, 0):
        response = requests.delete(f"{BASE_URL}/notes/{note_id}")

        assert note_id < 0
        assert response.status_code == 404

    for note_id in range(100000, 100010):
        response = requests.delete(f"{BASE_URL}/notes/{note_id}")

        assert note_id >= 100000
        assert response.status_code == 404



# -----------------------------------------------------
# Filter by category
# -----------------------------------------------------
def test_filter_by_category():
    category = "Work"

    for i in range(3):
        requests.post(f"{BASE_URL}/notes", json={
            "title": f"Work Note {i}",
            "content": "Content",
            "category": category,
            "tags": []
        })

    response = requests.get(f"{BASE_URL}/notes?category={category}")

    assert response.status_code == 200

    data = response.json()

    for note in data:
        assert note["category"] == category

# Category nonexistend
def test_filter_by_nonexistent_category():
    for i in range(100000, 100005):
        category = f"Category_{i}"

        response = requests.get(f"{BASE_URL}/notes?category={category}")

        assert response.status_code == 200
        assert response.json() == []


# -----------------------------------------------------
# POST /notes - Validation Error (fehlende Pflichtfelder)
# -----------------------------------------------------
def test_create_note_missing_fields():
    invalid_notes = [
        {
            "content": "Kein Titel",
            "category": "Test",
            "tags": []
        },
        {
            "title": "Kein Content",
            "category": "Test",
            "tags": []
        },
        {
            "title": "Kein Category",
            "content": "Content",
            "tags": []
        }
    ]

    for note_data in invalid_notes:
        response = requests.post(f"{BASE_URL}/notes", json=note_data)

        assert response.status_code == 422


# -----------------------------------------------------
# FILTER: search (Normalfall)
# -----------------------------------------------------
def test_filter_by_search():
    keyword = "meeting"

    # Notes erstellen (eine enthält keyword)
    requests.post(f"{BASE_URL}/notes", json={
        "title": "Meeting Note",
        "content": "Wir haben ein meeting",
        "category": "Work",
        "tags": []
    })

    requests.post(f"{BASE_URL}/notes", json={
        "title": "Random Note",
        "content": "Irgendwas anderes",
        "category": "Other",
        "tags": []
    })

    response = requests.get(f"{BASE_URL}/notes?search={keyword}")

    assert response.status_code == 200

    data = response.json()

    for note in data:
        assert keyword in note["title"].lower() or keyword in note["content"].lower()


# -----------------------------------------------------
# FILTER: search
# -----------------------------------------------------
def test_filter_search_no_results():
    for i in range(100000, 100005):
        keyword = f"keyword_{i}"

        response = requests.get(f"{BASE_URL}/notes?search={keyword}")

        assert response.status_code == 200
        assert response.json() == []


# -----------------------------------------------------
# FILTER: tag 
# -----------------------------------------------------
def test_filter_by_tag():
    tag = "important"

    requests.post(f"{BASE_URL}/notes", json={
        "title": "Tag Note",
        "content": "Mit Tag",
        "category": "Test",
        "tags": [tag]
    })

    response = requests.get(f"{BASE_URL}/notes?tag={tag}")

    assert response.status_code == 200

    data = response.json()

    for note in data:
        assert tag in note["tags"]


# tag nonexistent
def test_filter_by_nonexistent_tag():
    for i in range(100000, 100005):
        tag = f"tag_{i}"

        response = requests.get(f"{BASE_URL}/notes?tag={tag}")

        assert response.status_code == 200
        assert response.json() == []


# -----------------------------------------------------
# FILTER: combined filters
# -----------------------------------------------------
def test_combined_filters():
    category = "Work"
    tag = "urgent"
    keyword = "task"

    requests.post(f"{BASE_URL}/notes", json={
        "title": "Important Task",
        "content": "Dringende task",
        "category": category,
        "tags": [tag]
    })

    response = requests.get(
        f"{BASE_URL}/notes?category={category}&tag={tag}&search={keyword}"
    )

    assert response.status_code == 200

    data = response.json()

    for note in data:
        assert note["category"] == category
        assert tag in note["tags"]
        assert keyword in note["title"].lower() or keyword in note["content"].lower()


# -----------------------------------------------------
# FILTER: date-based filtering
# -----------------------------------------------------
def test_filter_by_date():
    note_data = {
        "title": "Date Filter Note",
        "content": "Diese Note wird für den Datumsfilter benutzt",
        "category": "DateTest",
        "tags": ["date"]
    }

    create_response = requests.post(f"{BASE_URL}/notes", json=note_data)
    assert create_response.status_code == 201

    created_note = create_response.json()
    created_at = created_note["created_at"]

    response = requests.get(
        f"{BASE_URL}/notes?created_after=2000-01-01&created_before=2999-12-31"
    )

    assert response.status_code == 200

    data = response.json()
    note_ids = []

    for note in data:
        note_ids.append(note["id"])

    assert created_note["id"] in note_ids


# -----------------------------------------------------
# FILTER: date-based filtering (Grenzfall)
# -----------------------------------------------------
def test_filter_by_date_no_results():
    response = requests.get(
        f"{BASE_URL}/notes?created_before=1900-01-01"
    )

    assert response.status_code == 200
    assert response.json() == []
    

# -----------------------------------------------------
# GET /notes/stats
# -----------------------------------------------------
def test_notes_statistics():
    response = requests.get(f"{BASE_URL}/notes/stats")

    assert response.status_code == 200

    data = response.json()

    assert "total_notes" in data
    assert "by_category" in data
    assert "top_tags" in data
    assert "unique_tags_count" in data


# -----------------------------------------------------
# GET /categories
# -----------------------------------------------------
def test_list_categories():
    response = requests.get(f"{BASE_URL}/categories")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# -----------------------------------------------------
# GET /categories/{category}/notes
# -----------------------------------------------------
def test_notes_by_category():
    category = "School"

    requests.post(f"{BASE_URL}/notes", json={
        "title": "School Note",
        "content": "Content",
        "category": category,
        "tags": []
    })

    response = requests.get(f"{BASE_URL}/categories/{category}/notes")

    assert response.status_code == 200

    data = response.json()

    for note in data:
        assert note["category"] == category


# -----------------------------------------------------
# PATCH /notes/{id}
# -----------------------------------------------------
def test_patch_note_title_only():
    note_data = {
        "title": "Original",
        "content": "Content",
        "category": "Test",
        "tags": []
    }

    create_response = requests.post(f"{BASE_URL}/notes", json=note_data)
    note_id = create_response.json()["id"]

    patch_data = {
        "title": "Patched Title"
    }

    response = requests.patch(f"{BASE_URL}/notes/{note_id}", json=patch_data)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Patched Title"
    assert data["content"] == "Content"


# nonexistent note
def test_patch_nonexistent_note():
    for note_id in range(-10, 0):
        response = requests.patch(f"{BASE_URL}/notes/{note_id}", json={"title": "X"})
        assert response.status_code == 404

    for note_id in range(100000, 100010):
        response = requests.patch(f"{BASE_URL}/notes/{note_id}", json={"title": "X"})
        assert response.status_code == 404