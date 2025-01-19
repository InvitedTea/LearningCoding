# Lesson 1: Introduction to Lists
# Theme: Making a Pokemon/Trading Card Collection

# Creating a list of favorite things
my_pokemon = ["Pikachu", "Charizard", "Bulbasaur"]

# Adding to our collection
my_pokemon.append("Squirtle")  # Adding one Pokemon
print("My Pokemon collection:", my_pokemon)

# Finding out how many Pokemon we have
number_of_pokemon = len(my_pokemon)
print("I have", number_of_pokemon, "Pokemon!")

# Checking if a Pokemon is in our collection
if "Pikachu" in my_pokemon:
    print("Yes, I have Pikachu!")