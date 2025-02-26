import pytest
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_endpoint(client):
    response = client.get('/')
    data = response.get_json()
    
    assert response.status_code == 200
    assert 'message' in data
    assert 'Hello from Python Flask application!' in data['message']
    assert 'hostname' in data
    assert 'version' in data

def test_health_endpoint(client):
    response = client.get('/health')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['status'] == 'healthy'