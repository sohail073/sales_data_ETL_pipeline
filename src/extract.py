import requests

def extract_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()
