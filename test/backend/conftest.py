import os
import tempfile

import pytest
from flask import Flask
from flask_cors import CORS
from src.backend.controller.controller import Controller
from src.backend.server import app

@pytest.fixture(scope='module')
def test_client():
    test_app = app

    with test_app.test_client() as test_client:
        with test_app.app_context():
            yield test_client
