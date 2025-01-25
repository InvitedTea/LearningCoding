# Pokemon Game Assignment
# Your name: _____________
# Date: _________________

import random
import time

# Task 1: Add 3 more Pokemon to this list
pokemon_list = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Meowth"]
# Add your Pokemon here:
# 1. 
# 2. 
# 3. 

def pokemon_party():
    """
    Task 2: Create a Pokemon party!
    Make 4 Pokemon play fun games together
    Don't forget to add fun emoji! 🎮
    """
    # Write your code here:
    print("Welcome to the Pokemon party! 🎉")
    
    # Pick 4 random Pokemon
    
    # Make them play games
    
    # Add fun messages and emoji!

# Task 3: Test your game
def play_game():
    print("=== Welcome to Pokemon World! ===")
    
    while True:
        print("\nWhat would you like to do?")
        print("1: Meet a Pokemon")
        print("2: Have a party!")
        print("3: Exit")
        
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            # Find a random Pokemon
            pokemon = random.choice(pokemon_list)
            print(f"You found a {pokemon}! ⭐")
        elif choice == "2":
            pokemon_party()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Please type 1, 2, or 3")

# Start the game!
play_game()