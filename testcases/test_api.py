import requests

def test_get_posts_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

def test_get_posts_response_type():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert isinstance(response.json(), list)