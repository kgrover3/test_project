import requests

def get_json(url: str) -> dict:
    """Fetch JSON from a URL and return it as a dict."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
