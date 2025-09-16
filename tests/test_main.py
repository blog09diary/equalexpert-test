# Import required modules for testing
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import httpx
import sys
import os

# Add the parent directory to the system path to import 'main'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import app

# Create a test client using the FastAPI app
client = TestClient(app)

# Test fetching public gists for the user 'octocat'
def test_get_gists_octocat():
    mock_gists = [
        {"id": "1", "description": "Test Gist", "html_url": "https://gist.github.com/octocat/1"}
    ]
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_response = httpx.Response(
            status_code=200,
            json=mock_gists
        )
        mock_get.return_value = mock_response
        response = client.get("/octocat")
        # Ensure the response is successful
        if response.status_code != 200:
            raise AssertionError(f"Expected status 200, got {response.status_code}")
        # The response should be a list
        if not isinstance(response.json(), list):
            raise AssertionError("Response is not a list")
        # If there are gists, check for required fields
        if response.json():
            gist = response.json()[0]
            if "id" not in gist:
                raise AssertionError("'id' not in gist")
            if "url" not in gist:
                raise AssertionError("'url' not in gist")