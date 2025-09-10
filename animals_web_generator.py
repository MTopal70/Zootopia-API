import json

import requests


def fetch_animals_from_api(query):
    """API call for animals with specific amen."""
    url = f"https://api.api-ninjas.com/v1/animals?name={query}"
    headers = {"X-Api-Key": "4H21ggbBhTMC1opbfp8FVQ==Bc3M4B0xYTu9ofQw"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        return []



def get_available_skin_types(data):
    """returns a sorted list with all the available skin types."""
    skin_types = set()
    for animal in data:
        skin = animal.get("characteristics", {}).get("skin_type")
        if skin:
            skin_types.add(skin)
    return sorted(skin_types)


def serialize_animal(animal_obj):
    """creates a HTML for each animal object"""
    name = animal_obj.get("name")
    taxonomy = animal_obj.get("taxonomy", {})
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    html = '<li class="cards__item">\n'
    if name:
        html += f'  <div class="card__title">{name}</div>\n'
    html += '  <div class="card__text">\n'
    html += '    <ul class="card__details">\n'

    if characteristics.get("diet"):
        html += f'      <li class="card__detail"><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if locations:
        html += f'      <li class="card__detail"><strong>Location:</strong> {locations[0]}</li>\n'
    if characteristics.get("type"):
        html += f'      <li class="card__detail"><strong>Type:</strong> {characteristics["type"]}</li>\n'
    if taxonomy.get("scientific_name"):
        html += f'      <li class="card__detail"><strong>Scientific Name:</strong> {taxonomy["scientific_name"]}</li>\n'
    if characteristics.get("lifespan"):
        html += f'      <li class="card__detail"><strong>Lifespan:</strong> {characteristics["lifespan"]}</li>\n'
    if characteristics.get("skin_type"):
        html += f'      <li class="card__detail"><strong>Skin Type:</strong> {characteristics["skin_type"]}</li>\n'
    if characteristics.get("slogan"):
        html += f'      <li class="card__detail"><em>{characteristics["slogan"]}</em></li>\n'

    html += '    </ul>\n'
    html += '  </div>\n'
    html += '</li>\n'
    return html


def generate_html(data, template_path, output_path):
    """creates the final HTML file with all the animal cards."""
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    cards_html = "".join(serialize_animal(animal) for animal in data)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def main():
    query = input("Enter a name of an animal: ").strip()
    animals_data = fetch_animals_from_api(query)

    if not animals_data:
        print("No data received from API.")
        return

    generate_html(animals_data, "animals_template.html", "animals.html")
    print("Website was successfully generated to the file animals.html.")

    skin_types = get_available_skin_types(animals_data)

    print("Available Skin Types:")
    for skin in skin_types:
        print(f"- {skin}")

    selected = input("\nPlease enter a Skin Type : ").strip()

    # filter animals
    filtered_animals = [
        animal for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type") == selected
    ]

    if not filtered_animals:
        print(f"No animals with Skin Type '{selected}' found.")
    else:
        generate_html(filtered_animals, "animals_template.html", "animals.html")
        print(f"Created animals.html with Skin Type '{selected}' successfully.!")


if __name__ == "__main__":
    main()

