# 08random_assignment_simplified.py
import random
import time

pokemon_list = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Meowth"]

def encounter_pokemon():
    """Encounters a random Pokemon and tells you its type."""

    pokemon = random.choice(pokemon_list)
    print(f"\nYou encountered a wild {pokemon}!")

    # Simple type assignment (for demonstration)
    if pokemon == "Pikachu":
        pokemon_type = "Electric"
    elif pokemon == "Charmander":
        pokemon_type = "Fire"
    elif pokemon == "Squirtle":
        pokemon_type = "Water"
    elif pokemon == "Bulbasaur":
        pokemon_type = "Grass"
    else:
        pokemon_type = "Normal"

    print(f"It's a {pokemon_type} type Pokemon!")
    time.sleep(1)  # Pause for a moment

# Encounter a few Pokemon
for _ in range(3):  # Encounter 3 Pokemon
    encounter_pokemon()



def pokemon_race():
  """A simple race between two random Pokemon"""

  pokemon1 = random.choice(pokemon_list)
  pokemon2 = random.choice(pokemon_list)

 # Ensure different Pokemon are chosen
  while pokemon1 == pokemon2:
        pokemon2 = random.choice(pokemon_list)


  print(f"\n{pokemon1} and {pokemon2} are racing!")
  time.sleep(1)

  # Simulate the race (randomly choose a winner)
  winner = random.choice([pokemon1, pokemon2])

  print("...")  # Suspense!
  time.sleep(2)
  print(f"{winner} wins the race!")

# Have a Pokemon race
pokemon_race()