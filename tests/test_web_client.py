"""Test API End Points"""
from fastapi.testclient import TestClient
import pytest
from main import app
from app_logic.apho_gen import partial_texts

client = TestClient(app)

def test_get_apho_api():
    name = "Peter"
    response = client.get(f'v1/feel-good/{name}')
    message = response.json()['message']
    assert name in message
    assert any(p in message for p in partial_texts)
    
def test_plur_api():
    text = "here comes the rain again. this these that those"
    response = client.get(f'v1/pluralize/{text}')
    data = response.json()['data']
    assert data == {'here': 'heres', 'comes': 'comess', 'the': 'thes', 'rain': 'rains', 'again': 'agains', 'this': 'these', 'these': 'theses', 'that': 'those', 'those': 'thoses'}