import json
import os
import tempfile

import pytest
from flask import Flask
from flask_cors import CORS
from src.backend.controller.controller import Controller
from src.backend.server import app







def test_server_start(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_post_data(test_client):
    request_body = {
        "algorithm": "Dijkstra",
        "start": "Brandywine Dr, Amherst, MA 01002",
        "dest": "Rolling Green Drive, Amherst, MA 01002",
        "mode": "max",
        "limit": 50,
        "city": "Amherst"
    }
    expected_response = {

    }
    request_json = json.dumps(request_body)
    response = test_client.post('/route',
                             data=request_json,
                             content_type='application/json')
    print(response.get_json())



def test_home_page():
    with test_app.test_client() as test_client:
        response = test_client.get('/')
        print(response)
        yield test_client
