# Assignment: Create Your Own Trading Card Game System!
# ===================================================

# Task 1: Create Your Card Collection
# ---------------------------------
# Create a list of at least 5 character cards
# Each card should be a dictionary with these properties:
# - name
# - power (number between 1-100)
# - type (like "Fire", "Water", "Earth", etc.)
# - special_move

# Example to get started:
my_cards = [
    {
        "name": "Dragon Fighter",
        "power": 75,
        "type": "Fire",
        "special_move": "Flame Blast"
    }
]

# Task 2: Card Management
# ----------------------
# Write code to:
# 1. Add a new card to your collection
# 2. Find your strongest card
# 3. Count how many cards you have of each type
# 4. Calculate the average power of your cards

# Task 3: Battle System
# --------------------
# Create a simple battle system that:
# 1. Takes two cards
# 2. Compares their power
# 3. Declares a winner
# Bonus: Add type advantages (like Water beats Fire)