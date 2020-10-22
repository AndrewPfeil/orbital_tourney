import numpy as np 

# test parameters
number_of_participants = 8

# initialize start rings
standard_seed = {}
collated_seed = {}

# generate seeded initial rings
def generate_standard_seed(number_of_participants):
    
    
    for i in range(number_of_participants):
        standard_seed["Player" + str(i)] = {
            "seed": i+1,
            "position": i+1,
            "ring": 0
        }

def generate_collated_seed(number_of_participants):
    initial_seed = np.array([*range(number_of_participants)])
    split_seed = np.array_split(initial_seed,2)
    flip_second = np.flip(split_seed[1])
    collated_seed_order = np.empty([number_of_participants])

    for i in range(number_of_participants):
        if (i % 2) == 0:
            collated_seed_order[i] = split_seed[0][int(i/2)]
        else:
            collated_seed_order[i] = flip_second[int(i/2)]

    
    for i in range(number_of_participants):    
        collated_seed["Player" + str(int(collated_seed_order[i] + 1))] = {
            "seed": int(collated_seed_order[i] + 1),
            "position": i+1,
            "ring": 0
        }

    print(collated_seed)

generate_standard_seed(number_of_participants)
generate_collated_seed(number_of_participants)
    
    