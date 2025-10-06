# Author: Carter Roberts
# Institution: Loyola University New Orleans
# Instructor: Dr. Omar EL Khatib
# Filename: roberts_knapsack.py
# Description: Uses simulated annealing to solve
# knapsack problem
# Date Created: 10/6/2025
# Date Modified: 10/6/2025

import random
from math import exp

# 'object': (weight, value)
Objects = {'A': (10, 2), 'B': (6, 3), 'C': (4, 8),
           'D': (8, 5), 'E': (9, 5), 'F': (7, 6)}
# capacity
C = 15
# list of all the 'object' titles
Items = list(Objects.keys())
# number of objects
nObjects = len(Objects)

def Value(state):
    # write your code here
    # Hint: you will need to use Items list to access the
    #       Objects weights and values
    # initialize numerics for weight and value of sack
    val = 0
    weight = 0
    # go through each item in state
    for index, i in enumerate(state):
        # check first if illegal/overcapacity weight
        if weight > C:
            return -1
        # if the item is used,
        if i == 1:
            # get what that item's letter key is
            itemTitle = Items[index]
            # get the weight and value for that key
            item = Objects[itemTitle]
            # add that weight and value to the numerics
            weight += item[0]
            val += item[1]
    # check one last time if illegal/overcapacity weight
    if weight > C:
        return -1

    # give the value since it's legal if weight never > C
    return val     

def get_neighbor(state):
    n = len(state)
    k = random.randint(0, n-1)
    j = state[k]
    # swap that bool value for that index
    if j == 1: j = 0
    elif j == 0: j = 1
    # then actually change it in the copied new state
    new_state = state.copy()
    new_state[k] = j
    return new_state
    
def simulated_annealing(state):
    t = 4000
    alpha = 0.99
    while t > 0:
        newState = get_neighbor(state)
        stateVal = Value(state)
        newStVal = Value(newState)
        # since 13 is highest possible score here
        if newStVal == 13: return newState
        if newStVal >= stateVal:
            state = newState
        else:
            r = random.uniform(0, 1)
            # this will always be negative here
            deltaE = newStVal - stateVal
            # so this is kind of redundant, always happens
            # but I keep it because I'm scared
            if r < exp(deltaE / t):
                state = newState
        # lower temperature
        t *= alpha
    return state
    
bestValue = -1
bestState = []
for k in range(40):
    state = [random.randrange(2) for k in range(nObjects)]
    random.shuffle(state)
    state = simulated_annealing(state)
    v = Value(state)
    
    if bestValue < v:
        bestValue = v
        bestState = state
print('best state found: ', bestState, bestValue)
    
