#Pokedex

import requests
from time import sleep

pokemon_name = input('Enter the name of the Pokémon:\n').lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

response = requests.get(url)


#Pokemon
if response.status_code == 200:
    print("="*50)
    sleep(1)
    print("Pokémon found!")
    sleep(1)
    print(f'Analysing {pokemon_name.title()}...')
    print("="*50)
    sleep(1)
    print('Results:\n')
    pokemon_data = response.json()
    
    name = pokemon_data['name'].capitalize()
    print(f"Nome: {name}")

    dex_number = pokemon_data['id']
    print(f'Dex number: {dex_number}')
    
    # Types
    print("Type(s):")
    for typings in pokemon_data['types']:
        pokemon_type = typings['type']['name'].capitalize()
        print(f"- {pokemon_type}")

    url_species = pokemon_data['species']['url']
    
    response_species = requests.get(url_species)
    
    if response_species.status_code == 200:
        species_data = response_species.json()
        description = "English description not found!"
        
        # Dex Entry
        for entrada in species_data['flavor_text_entries']:
            if entrada['language']['name'] == 'en':
                description = entrada['flavor_text']
                break 
        
        # Data cleaning
        clean_description = description.replace('\n', ' ').replace('\f', ' ')
        print(f"\nDescription:\n{clean_description}")
        
else:
    print("Pokémon not found. Please try again!")