# Lesson 3: Introduction to Dictionaries
# Theme: Pokemon Character Stats

# Creating a Pokemon character card
pikachu = {
    "name": "Pikachu",
    "type": "Electric",
    "power": 55,
    "special_move": "Thunder Bolt"
}

# Adding new information
pikachu["speed"] = 90

# Accessing information
print(f"{pikachu['name']} is a {pikachu['type']} type Pokemon!")
print(f"Its special move is {pikachu['special_move']}!")

# Creating multiple character cards
pokemon_cards = {
    "Pikachu": {"type": "Electric", "power": 55},
    "Charizard": {"type": "Fire", "power": 85},
    "Squirtle": {"type": "Water", "power": 50}
}

# Finding the strongest Pokemon
strongest_pokemon = ""
max_power = 0

for pokemon, stats in pokemon_cards.items():
    if stats["power"] > max_power:
        strongest_pokemon = pokemon
        max_power = stats["power"]

print(f"The strongest Pokemon is {strongest_pokemon} with power {max_power}!")