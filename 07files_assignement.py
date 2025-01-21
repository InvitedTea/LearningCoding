# Lesson 7 Homework: My Pokemon Journal
# Your goal: Create a Pokemon journal that can save and load your Pokemon adventures!

# Here's some code to help you get started:

# PART 1: Writing Your First Journal Entry
# --------------------------------------
print("=== My Pokemon Journal ===")

# Ask about today's adventure
trainer_name = input("What's your name? ")
location = input("Where did you explore today? ")
pokemon_seen = input("What Pokemon did you see? ")

# TODO: Save this information to a file called "pokemon_journal.txt"
# Hint: Use with open("pokemon_journal.txt", "w") as file:

# PART 2: Adding More Adventures
# ----------------------------
print("\nLet's add another adventure!")

# TODO: Add a new entry to your journal
# But don't erase the old one!
# Hint: Use "a" instead of "w" when opening the file

# PART 3: Reading Your Journal
# --------------------------
print("\nLet's read your journal!")

# TODO: Read and show all your adventures
# Hint: Use with open("pokemon_journal.txt", "r") as file:

# BONUS CHALLENGES:
# 1. Add the date to each entry
# 2. Let trainers add Pokemon to their collection
# 3. Add special items they found
# 4. Add pictures (using ASCII art!) to your journal entries

# Example of how your journal might look:
"""
=== POKEMON JOURNAL ===
Trainer: Ash
Location: Viridian Forest
Pokemon Seen: Caterpie, Weedle
-------------------
Trainer: Ash
Location: Pewter City
Pokemon Seen: Geodude
-------------------
"""