# Lesson 4: Loops and Game Mechanics
# Theme: Pokemon Training Games

# Creating a training game using while loops
pokemon_exp = 0
training_days = 1

print("Let's train your Pokemon!")
while pokemon_exp < 100:
    # Training activities
    print(f"\nDay {training_days} of training:")
    print("Choose a training activity:")
    print("1. Battle (gain 20 exp)")
    print("2. Run (gain 10 exp)")
    print("3. Rest (gain 5 exp)")
    
    # Using input to make it interactive
    choice = input("What would you like to do? (1/2/3): ")
    
    if choice == "1":
        pokemon_exp += 20
        print("Great battle! Your Pokemon gained 20 exp!")
    elif choice == "2":
        pokemon_exp += 10
        print("Good exercise! Your Pokemon gained 10 exp!")
    else:
        pokemon_exp += 5
        print("Nice rest! Your Pokemon gained 5 exp!")
    
    print(f"Total experience: {pokemon_exp}/100")
    training_days += 1

print(f"\nCongratulations! Your Pokemon is fully trained after {training_days-1} days!")

# Using for loops with lists
pokemon_types = ["Fire", "Water", "Grass", "Electric"]
print("\nLearning about Pokemon types:")

for type_name in pokemon_types:
    if type_name == "Fire":
        print(f"{type_name} is strong against Grass!")
    elif type_name == "Water":
        print(f"{type_name} is strong against Fire!")
    elif type_name == "Grass":
        print(f"{type_name} is strong against Water!")
    else:
        print(f"{type_name} is strong against Water types!")

# Nested loops for making a simple game board
print("\nCreating a Pokemon game board:")
board_size = 3

for row in range(board_size):
    for col in range(board_size):
        if row == 1 and col == 1:
            print("P", end=" ")  # P for Pokemon
        else:
            print(".", end=" ")  # Empty space
    print()  # New line after each row