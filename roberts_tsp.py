# Author: Carter Roberts
# Institution: Loyola University New Orleans
# Instructor: Dr. Omar EL Khatib
# Filename: roberts_tsp.py
# Description: Uses random restart hill climbing
# to solve travel salesman problem with 4 cities
# Date Created: 10/5/2025
# Date Modified: 10/5/2025

import random

MAX_TRIALS = 100

tsp = [[0, 400, 500, 300],
       [400, 0, 300, 500],
       [500, 300, 0, 400],
       [300, 500, 400, 0]
       ]
cities = len(tsp)

def Value(state):
    # make sure scope of distVal is whole func
    distVal = 0
    # go through all of state except last,
    for c in range(len(state) - 1):
        # and get matrix value toward next
        distVal += tsp[state[c]][state[c+1]]
    # which is done outside loop
    first = state[0]
    last = state[3]
    distVal += tsp[last][first]
    # give back distance value
    return distVal
    
def get_neighbor(state):
    n = len(state)
    # make equal the values to hold indexes to swap
    k = 1
    l = 1
    # while these are equal, assign them two random index in state
    while k == l:
        k = random.randint(0, n-1)
        l = random.randint(0, n-1)
    new_state = state.copy()
    # swap values in new state based on old positions in old state
    new_state[k] = state[l]
    new_state[l] = state[k]
    # give back new state
    return new_state
    
    

def hill_climbing(state):
    trial = 0
    while trial < MAX_TRIALS:
        new_state = get_neighbor(state)
        if Value(new_state) <= Value(state):
            state = new_state
        trial += 1
    return state

best_state = []
best_dist = 100000
for k in range(20):
    state = list(range(cities))
    random.shuffle(state)
    state = hill_climbing(state)
    v = Value(state)
    if best_dist > v:
        best_dist = v
        best_state = state
    
print(best_state, best_dist)
