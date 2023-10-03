import requests

characters = []

for i in range(10):
    url = f"https://pokeapi.co/api/v2/pokemon/{i+1}"
    resp = requests.get(url)
    if resp.status_code == 200:
        json_data = resp.json()
        characters.append(
            (json_data["name"],
             json_data["height"])
        )
    else:
        characters.append("error!")

print(characters)
