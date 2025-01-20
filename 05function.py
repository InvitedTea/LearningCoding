Functions# Lesson 5: Introduction to Functions
# Theme: Pokemon Battle System

# Creating our first function
def greet_pokemon(pokemon_name):
    print(f"Go, {pokemon_name}!")
    print("It's battle time!")

# Using our function
greet_pokemon("Pikachu")
greet_pokemon("Charizard")

# Function with return value
def calculate_damage(power, effectiveness):
    damage = power * effectiveness
    return damage

# Battle function with multiple parameters
def pokemon_battle(attacker_name, attacker_power, defender_name, effectiveness):
    print(f"\n{attacker_name} is attacking {defender_name}!")
    
    # Calculate and return damage
    damage = calculate_damage(attacker_power, effectiveness)
    
    print(f"Attack power: {attacker_power}")
    print(f"Effectiveness: {effectiveness}")
    print(f"Total damage: {damage}")
    
    return damage

# Create a simple healing function
def heal_pokemon(pokemon_name, current_hp):
    heal_amount = 20
    new_hp = current_hp + heal_amount
    print(f"\nHealing {pokemon_name}...")
    print(f"Restored {heal_amount} HP!")
    print(f"New HP: {new_hp}")
    return new_hp

# Lets have a Pokemon battle!
print("Welcome to the Pokemon Battle System!")

# Test our battle system
battle_damage = pokemon_battle("Pikachu", 55, "Squirtle", 2.0)
print(f"Battle resulted in {battle_damage} damage!")

# Test our healing system
pokemon_hp = 30
print(f"\nPikachu is hurt! Current HP: {pokemon_hp}")
pokemon_hp = heal_pokemon("Pikachu", pokemon_hp)

# Bonus: Create a function that checks if a Pokemon won
def check_victory(pokemon_hp):
    if pokemon_hp > 0:
        return True
    return False

# Test the victory check
is_winner = check_victory(pokemon_hp)
if is_winner:
    print("\nYour Pokemon is still ready to battle!")
else:
    print("\nYour Pokemon needs to rest!")