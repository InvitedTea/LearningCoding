# Lesson 7: Saving and Loading Pokemon Data
# Theme: Creating a Pokedex!

# First, let's learn to write to a file
print("Let's create your Pokemon collection file!")

# Writing to a file
my_pokemon = ["Pikachu", "Charizard", "Squirtle"]
print("Saving your Pokemon...")

# Open file and write to it
with open("my_pokemon.txt", "w") as file:
    for pokemon in my_pokemon:
        file.write(pokemon + "\n")

print("Pokemon saved!")

# Reading from a file
print("\nLet's read your Pokemon collection:")
with open("my_pokemon.txt", "r") as file:
    pokemon_list = file.readlines()  # Read all lines

print("Your Pokemon:")
for pokemon in pokemon_list:
    print("- " + pokemon.strip())  # strip() removes extra spaces and \n

# Let's create a simple Pokedex entry
print("\nLet's add a new Pokemon to your Pokedex!")
pokemon_name = input("Enter Pokemon name: ")
pokemon_type = input("Enter Pokemon type: ")
pokemon_level = input("Enter Pokemon level: ")

# Save the Pokedex entry
with open("pokedex.txt", "a") as file:  # 'a' means append - add to end
    file.write(f"{pokemon_name},{pokemon_type},{level}\n")

print("Pokedex updated!")

# Reading the Pokedex
print("\nReading Pokedex entries:")
with open("pokedex.txt", "r") as file:
    pokedex_entries = file.readlines()

for entry in pokedex_entries:
    name, type_, level = entry.strip().split(",")
    print(f"Pokemon: {name}")
    print(f"Type: {type_}")
    print(f"Level: {level}")
    print("-" * 20)

# Creating a Pokemon save file
print("\nSaving your game progress...")
trainer_name = input("What's your name? ")
badges = input("How many badges do you have? ")

# Save game progress
with open(f"{trainer_name}_save.txt", "w") as file:
    file.write(f"Trainer: {trainer_name}\n")
    file.write(f"Badges: {badges}\n")
    file.write("Pokemon:\n")
    for pokemon in my_pokemon:
        file.write(f"- {pokemon}\n")

print("Game progress saved!")