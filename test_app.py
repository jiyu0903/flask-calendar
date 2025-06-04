import pytest
from main import app, db, Event

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_event(client):
    response = client.post('/api/events', json={
        "title": "Test Event",
        "start": "2025-06-04 10:00",
        "end": "2025-06-04 12:00",
        "description": "A test event"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == "Test Event"
    assert data['start'] == "2025-06-04 10:00"

def test_get_event(client):
    post = client.post('/api/events', json={
        "title": "Read Event",
        "start": "2025-06-04 09:00",
        "end": "2025-06-04 11:00",
        "description": "To read"
    })
    event_id = post.get_json()['id']
    response = client.get(f'/api/events/{event_id}')
    assert response.status_code == 200
    assert response.get_json()['title'] == "Read Event"

def test_update_event(client):
    post = client.post('/api/events', json={
        "title": "Old Title",
        "start": "2025-06-04 08:00",
        "end": "2025-06-04 09:00"
    })
    event_id = post.get_json()['id']
    response = client.put(f'/api/events/{event_id}', json={
        "title": "Updated Title",
        "start": "2025-06-04 08:30",
        "end": "2025-06-04 09:30"
    })
    assert response.status_code == 200
    assert response.get_json()['title'] == "Updated Title"

def test_delete_event(client):
    post = client.post('/api/events', json={
        "title": "Delete Me",
        "start": "2025-06-04 13:00",
        "end": "2025-06-04 14:00"
    })
    event_id = post.get_json()['id']
    response = client.delete(f'/api/events/{event_id}')
    assert response.status_code == 204
    get = client.get(f'/api/events/{event_id}')
    assert get.status_code == 404

def test_get_all_events(client):
    client.post('/api/events', json={
        "title": "Event 1", "start": "2025-06-04", "end": "2025-06-05"
    })
    client.post('/api/events', json={
        "title": "Event 2", "start": "2025-06-06", "end": "2025-06-07"
    })
    response = client.get('/data')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2

# === Negative Tests ===

def test_create_event_missing_fields(client):
    response = client.post('/api/events', json={
        "start": "2025-06-04 10:00",
        "end": "2025-06-04 12:00"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "Missing fields" in data.get("error", "")

def test_get_nonexistent_event(client):
    response = client.get('/api/events/999')
    assert response.status_code == 404

def test_update_nonexistent_event(client):
    response = client.put('/api/events/999', json={
        "title": "Should Fail", "start": "x", "end": "y"
    })
    assert response.status_code == 404

def test_delete_nonexistent_event(client):
    response = client.delete('/api/events/999')
    assert response.status_code == 404
