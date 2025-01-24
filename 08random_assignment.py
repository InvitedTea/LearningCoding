# pokemon_mystery_assignment_08.py

import random
import time

# Pokemon and their corresponding locations (a little mystery!)
pokemon_locations = {
    "Pikachu": ["Viridian Forest", "Power Plant"],
    "Charmander": ["Mt. Ember", "Fiery Path"],
    "Squirtle": ["Cerulean Cave", "Vermilion City"],
    "Bulbasaur": ["Viridian Forest", "Cerulean City"],
    "Meowth": ["Route 5", "Pewter City"]  # Added Meowth with locations
}

items_list = ["Potion", "Poke Ball", "Rare Candy", "Great Ball", "Super Potion", "Ultra Ball"]  # More items


# Task 1: Create a function to find where a Pokemon might be
def find_pokemon(pokemon):
    """Finds the possible locations of a given Pokemon."""
    # TODO: Check if the Pokemon is in the pokemon_locations dictionary.
    # If it is, print its possible locations.
    # If not, print "That Pokemon is very mysterious! We don't know where it lives."

    time.sleep(1)  # Add a little suspense!




# Task 2: Create a function to search for items in a location
def search_location(location):
    """Searches a location for items."""
    print(f"\nSearching {location}...")
    time.sleep(2)  # More suspense!
    
    # TODO: Use random.choice() and random.randint() to find 1 to 3 random items from items_list
    # If no items are found, print "You didn't find anything this time."
    # If items are found print "You found: [item1, item2,... ]"


# Task 3: Create a "Pokemon Journey" function 
def pokemon_journey():
    """Takes the player on a Pokemon journey!"""
    print("Starting your Pokemon journey...")

    # TODO: 1. Choose a random Pokemon from pokemon_locations.keys()
    #       2. Use find_pokemon() to reveal its possible locations.
    #       3. Choose a random location from the Pokemon's possible locations
    #            (Hint: you might need to use random.choice() again).
    #       4. Use search_location() to look for items in that location.

pokemon_journey()