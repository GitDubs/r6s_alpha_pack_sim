#===============================================================================
# GitDubs
# 9 April 2020
#===============================================================================

import random

#Simulates how many games until an alpha pack roll hits
def simulate_alpha_pack_roll():
    #Assume one win out of every 3 games (1.5 + 1.5 + 2.0 = 5.0)
    games_per_win = 1
    percentage_adder = (1.5 * (games_per_win -1)) + 2.0

    
    #Always start with 5.0 because that is percent awarded on a win
    #after a successful alpha pack roll + the two games lost
    chance_to_hit = percentage_adder

    
    hit = False
    count = 0
    while not hit:
        roll = random.uniform(0, 100)
        hit = chance_to_hit >= roll
        chance_to_hit += percentage_adder
        count += games_per_win
    return count

highest_count = 0
cummulative_games = 0
num_simulations = 10000

#Run the simulation num_simulations times
for x in range(num_simulations):
    count = simulate_alpha_pack_roll()
    cummulative_games += count

    #Check if we have a new record for most games between successful rolls
    if count > highest_count:
        highest_count = count

#Print the average number of games and the most number of games between packs
print('average: ' + str(cummulative_games / num_simulations))
print('most games between packs: ' + str(highest_count))
