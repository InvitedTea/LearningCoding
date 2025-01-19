# Lesson 2: Working with Lists and Simple Algorithms
# Theme: Trading Card Game Scores

# Keeping track of game scores
game_scores = [10, 15, 8, 20, 12]

# Finding the highest score (introducing max())
highest_score = max(game_scores)
print("Your highest score is:", highest_score)

# Calculating average score (introducing sum and division)
total_score = sum(game_scores)
average_score = total_score / len(game_scores)
print("Your average score is:", average_score)

# Simple sorting algorithm (using a story)
# Let's arrange Pokemon cards by their power level
pokemon_powers = [50, 30, 80, 20, 60]
print("Unsorted powers:", pokemon_powers)

# Bubble sort explained like trading cards
for i in range(len(pokemon_powers)):
    for j in range(len(pokemon_powers) - 1):
        if pokemon_powers[j] > pokemon_powers[j + 1]:
            # Swap the cards if they're in the wrong order
            pokemon_powers[j], pokemon_powers[j + 1] = pokemon_powers[j + 1], pokemon_powers[j]

print("Sorted powers:", pokemon_powers)