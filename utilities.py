'''
Utility file that contains the functions to randomize a toon and trinket combo
Does not run anything by itself
'''
import random

'''
Picks a random toon from the list provided by toons.csv and returns it as a string
fails if toons.csv is not found
'''
def pick_toon():
    with open('toons.csv') as csvfile:
        toons = csvfile.read().strip().split(",")
        return random.choice(toons)

'''
Picks two random trinkets from the list provided by trinkets.csv and returns them as a list
fails if trinkets.csv is not found
'''
def pick_trinket():
    with open('trinkets.csv') as csvfile:
        trinkets = csvfile.read().strip().split(",")
        first = random.choice(trinkets)
        trinkets.remove(first)
        return [first, random.choice(trinkets)]