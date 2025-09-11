import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """API call for animals with specific amen.  API Key stored in secure way in .env file."""
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL + animal_name, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

