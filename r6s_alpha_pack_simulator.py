#===============================================================================
# GitDubs
# 9 April 2020
# Disclaimer: I wrote this according to my own understanding of the alpha pack
# system as of 04/09/2020, I am not a dev I was just bored, if you see some kind
# of issue with how it is working, write a better one I'm sure it's possible
#===============================================================================

import random

#Simulates how many games until an alpha pack roll hits
def simulate_alpha_pack_roll():
    #Assume one win out of every 3 games (1.5 + 1.5 + 2.0 = 5.0) 
    percentage_adder = 5.0

    #Always start with 5.0 because that is percent awarded on a win
    #after a successful alpha pack roll + the two games lost
    chance_to_hit = 5.0

    hit = False
    count = 0
    while not hit:
        roll = random.uniform(0, 100)
        hit = chance_to_hit >= roll
        chance_to_hit += percentage_adder
        count += 3
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
