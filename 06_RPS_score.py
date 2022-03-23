# RPS Component 6 - Soring System

#Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Resuklts for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# PLay Game 
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item

    if result == "tie":
        result == "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1


# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")