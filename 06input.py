# Lesson 6: Making Interactive Programs
# Theme: Pokemon Trainer Registration

# First, let's learn about getting input!
print("Welcome new Pokemon trainer!")

# Getting simple text input
trainer_name = input("What is your name? ")
print(f"Nice to meet you, {trainer_name}!")

# Getting numbers (with error checking)
age = input("How old are you? ")
while not age.isdigit():  # Makes sure they type a number
    print("Oops! Please type a number!")
    age = input("How old are you? ")
age = int(age)  # Convert string to number
print(f"Great! You are {age} years old!")

# Making choices
print("\nLet's choose your first Pokemon!")
print("1. Pikachu")
print("2. Charmander")
print("3. Squirtle")
print("4. Bulbasaur")

# Getting a valid choice
choice = input("Type the number of your choice (1-4): ")
while choice not in ['1', '2', '3', '4']:
    print("Oops! Please choose 1, 2, 3, or 4!")
    choice = input("Type the number of your choice (1-4): ")

# Using the choice
pokemon_names = {
    '1': 'Pikachu',
    '2': 'Charmander',
    '3': 'Squirtle',
    '4': 'Bulbasaur'
}
chosen_pokemon = pokemon_names[choice]
print(f"\nAwesome! {chosen_pokemon} is your first Pokemon!")

# Let's name our Pokemon!
pokemon_nickname = input(f"Would you like to give {chosen_pokemon} a nickname? (yes/no) ")
if pokemon_nickname.lower() == 'yes':
    nickname = input("What nickname would you like to give? ")
    print(f"Great! {chosen_pokemon} will now be called {nickname}!")
else:
    print(f"That's okay! {chosen_pokemon} is already a cool name!")

# Making a trainer card
print("\nCreating your trainer card...")
print("*" * 30)
print("POKEMON TRAINER CARD")
print(f"Name: {trainer_name}")
print(f"Age: {age}")
print(f"First Pokemon: {chosen_pokemon}")
print("*" * 30)

# Let's go on an adventure!
print("\nWould you like to:")
print("1. Train your Pokemon")
print("2. Look for wild Pokemon")
print("3. Rest at Pokemon Center")

adventure_choice = input("What would you like to do? (1/2/3) ")
while adventure_choice not in ['1', '2', '3']:
    print("Oops! Please choose 1, 2, or 3!")
    adventure_choice = input("What would you like to do? (1/2/3) ")

# Responding to their choice
if adventure_choice == '1':
    print(f"\nLet's train {chosen_pokemon}!")
    training_time = input("How many hours would you like to train? ")
    print(f"Great! After {training_time} hours of training, {chosen_pokemon} looks stronger!")
elif adventure_choice == '2':
    print("\nLet's look for wild Pokemon!")
    area = input("Where should we look? (forest/lake/cave) ")
    print(f"Adventure time! Let's explore the {area}!")
else:
    print("\nTime to rest at the Pokemon Center!")
    print("Nurse Joy welcomes you!")

# Ending our adventure
print("\nThanks for playing!")
ready = input("Ready for your next adventure? (yes/no) ")
if ready.lower() == 'yes':
    print("Great! See you next time!")
else:
    print("Take a good rest, trainer!")