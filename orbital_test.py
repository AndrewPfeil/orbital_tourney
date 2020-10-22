import numpy as np 

# test parameters
number_of_participants = 8
ordered_FLAG = False #False for collated

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
    
    print(seed)
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


    print(seed_order)
    print(round_lineup)
    #return round_lineup

#def execute_rounds(round_lineup):
    # for each player, search for unbattled neighbors
    # compute win vs loss, update seed{}, create and update temp round_wins{}
    # create and move players to appropriate rings (maintain position)
    # check for end condition (one player per ring)
    # repeat


    


setup_round(generate_seed(number_of_participants), ordered_FLAG, seed,number_of_participants)
#execute_rounds()
    
    