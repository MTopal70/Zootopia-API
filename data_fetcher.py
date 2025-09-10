import requests

API_KEY = "4H21ggbBhTMC1opbfp8FVQ==Bc3M4B0xYTu9ofQw"
API_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """Gets the animals data for the animal 'animal_name'.
        Returns: a list of animals, each animal is a dictionary.
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL + animal_name, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
