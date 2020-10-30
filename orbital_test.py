import numpy as np 
from random import *

# test parameters
number_of_participants = 8
ordered_FLAG = False #False for collated
win_condition = 'random' #seed, inverse_seed, random and realistic

# initialize start rings
seed = {}


# generate seeded initial ring for ordered seed
def generate_seed(number_of_participants):
    initial_seed_order = np.array([*range(number_of_participants)])
    split_seed = np.array_split(initial_seed_order,2)
    flip_second = np.flip(split_seed[1])
    collated_seed_order = np.empty([number_of_participants])

    for i in range(number_of_participants):
        if (i % 2) == 0:
            collated_seed_order[i] = split_seed[0][int(i/2)]
        else:
            collated_seed_order[i] = flip_second[int(i/2)]

    #prepare seed orders for setup function
    for i in initial_seed_order:
        initial_seed_order[i] = i+1
        collated_seed_order[i] = int(collated_seed_order[i])+1

    if ordered_FLAG == True:
        seed_order = initial_seed_order
    else: 
        seed_order = collated_seed_order
    seed_order = seed_order.astype(int)
 
    for i in range(number_of_participants):    
        seed["Player" + str(seed_order[i])] = {
            "seed": seed_order[i],
            "position": i+1,
            "ring": 0,
            "wins": 0,
            "losses": 0
        }
    
    #print(seed)
    return seed_order
    


def setup_round(seed_order, ordered_FLAG, seed, number_of_participants):
    #search dictionaries for rings and place players into them
    # possibly use matrix as structure with empty spaces for positions
    # numpy.vstack to add row to bottom or top and "move" players
    round_lineup = [0]*len(seed_order)

    for i in seed_order:
        for key in seed:
            if seed[key]['position'] == i:
                round_lineup[i-1] = key


    #print(seed_order)
    #print(round_lineup)
    return round_lineup

def execute_rounds(round_lineup, seed):
    # for each player, search for unbattled neighbors
    # create and move players to appropriate rings (maintain position)
    # check for end condition (one player per ring)
    # repeat
    round_records = {}

    for i in range(len(round_lineup)):
        for j in range(i + 1, len(round_lineup) +1):
            if i + 1 == len(round_lineup):
                compete(round_lineup[i], round_lineup[0],round_records)
                break
            elif round_lineup[j] == 0: 
                continue
            else:
                compete(round_lineup[i], round_lineup[j],round_records)
                break
    
    #print(round_records)

    update_seed(round_records)
    round_orbits = update_orbits()
    round_records.clear()

    

    for idx, row in enumerate(round_orbits):
        for position, col in enumerate(round_orbits[idx]):
            if np.count_nonzero(round_orbits[idx]) == 1:
                print(np.count_nonzero(round_orbits[idx]))
                break #move to next row if only one player in current row
            elif round_orbits[int(idx)][int(position)] == 0: 
                print("No player in row %s, col %s." % (idx, position))
                #break # to next position if current is empty
            else:
                competitor1 = round_orbits[int(idx)][int(position)]
                competitor2 = 0
                while competitor2 == 0:
                    competitor2 = next(round_orbits[int(idx)])
                compete(competitor1, competitor2, round_records)
                break

        print(np.count_nonzero(round_orbits[idx]))
    


def compete(competitor1, competitor2, round_records):
    # compute win vs loss, update seed{}, create and update temp round_wins{}
    print("%s faces %s in battle" % (competitor1, competitor2))
    #p = np.array([0,0],float)
    #x = np.array([0,0],float)

    if win_condition == 'seed':
        if seed[competitor1]['seed'] < seed[competitor2]['seed']:
            winner = competitor1
        else:
            winner = competitor2
    elif win_condition == 'inverse_seed':
        if seed[competitor1]['seed'] < seed[competitor2]['seed']:
            winner = competitor2
        else:
            winner = competitor1
    elif win_condition == 'random':
        x = randint(0,1)
        if x == 0:
            winner = competitor1
        else:
            winner = competitor2
    elif win_condition == 'realistic':
        c1_roll = 0
        c2_roll = 0

        while c1_roll == c2_roll:
            pc1_win = (number_of_participants - seed[competitor1]['seed'])/number_of_participants
            pc1_loss = seed[competitor1]['seed']/number_of_participants
            c1_roll = np.random.choice(a=[0,1], p=[pc1_win,pc1_loss])

            pc2_win = (number_of_participants - seed[competitor2]['seed'])/number_of_participants
            pc2_loss = seed[competitor2]['seed']/number_of_participants
            c2_roll = np.random.choice(a=[0,1], p=[pc2_win,pc2_loss])

        if c1_roll < c2_roll:
            winner = competitor1
        elif c1_roll > c2_roll:
            winner = competitor2
        else:
            print('roll error')
    else:
        print('Incorrect win_condition param.')
    
    if winner == competitor1:
        loser = competitor2
    elif winner == competitor2:
        loser = competitor1

    if winner not in round_records:
        round_records[winner] = {'wins': 1, 'losses': 0}
    elif winner in round_records:
        round_records[winner]['wins'] = (round_records[winner]['wins'] + 1)
    
    if loser not in round_records:
        round_records[loser] = {'wins': 0, 'losses': 1}
    elif loser in round_records:
        round_records[loser]['losses'] = (round_records[loser]['losses'] + 1)

        
    print("The winner is: ", winner)

def update_seed(round_records):
    for player in round_records:
        seed[player]['wins'] = seed[player]['wins'] + round_records[player]['wins']
        seed[player]['losses'] = seed[player]['losses'] + round_records[player]['losses']

        if round_records[player]['wins'] == 2:
            seed[player]['ring'] = seed[player]['ring'] + 1
        elif round_records[player]['losses'] == 2:
            seed[player]['ring'] = seed[player]['ring'] - 1
        
    #print(seed)

def update_orbits():
    rings = []
    for player in seed:
        if seed[player]['ring'] not in rings:
            rings.append(seed[player]['ring'])

    rings.sort()

    rows, cols = (len(rings), number_of_participants)
    round_orbits = [[0 for i in range(cols)] for j in range(rows)]

    for player in seed:
        for x in range(len(rings)):
            if seed[player]['ring'] == rings[x]:
                round_orbits[x][(seed[player]['position'] - 1)] = player


    for row in round_orbits:
        print(row)
    

    print(rings)
    return round_orbits

    
execute_rounds(setup_round(generate_seed(number_of_participants), ordered_FLAG, seed,number_of_participants),seed)
    
    