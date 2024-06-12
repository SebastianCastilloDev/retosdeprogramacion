import requests

"""
Ejercicio
"""

response = requests.get("https://pokeapi.co")

# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Error en la petición")
#     print(response.status_code)
#     print(response.text)

pokemon = input("Introduce el nombre del pokemon: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

if response.status_code == 200:
    data = response.json()
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    for type in data["types"]:
        print("Tipo(s): ", type["type"]["name"] )
else:
    print("Error en la petición")
    print(response.status_code)
    print(response.text)
