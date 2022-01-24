# Question 1
# B. 

from pickle import LIST
from typing import List
from function_exercises import calculate_tip

calculate_tip(.18, 100)
calculate_tip(.20, 100)
calculate_tip(.21, 45)

# Question 2

# How many different ways can you combine the letters
# from "abd" with the numbers 1, 2, and 3?

import itertools

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

combination = itertools.product(letters, numbers)
for pairing in combination:
    print(pairing)

# 9 different ways

# How many different ways can you combine two 
# of the letters from "abcd"?

len(list(itertools.combinations("abcd", 2)))

# 6 combinations 

# How many different permutations are there of
# 2 letters from "abcd?

letters_list = 'abcd'
letters_permutated = list(itertools.permutations(letters_list))
print(len(letters_permutated))

# 24 permutations 

# Question 3 

import json

profiles = list(json.load(open('profiles.json'))) 
#importing json dictionaries into list

print(profiles[0].keys())
print(profiles[0].values())

# Number of users

number_users = len(profiles)
print(number_users)

# 19 

# Number of active users

def active_users():
    i = 0
    for profile in profiles:
        if profile["isActive"]:
            i += 1
    return i 

active_users()

# 9 active users

# Number of inactive users

inactive_users = [profile for profile in profiles if not profile['isActive']]
print(len(inactive_users))
# 10 inactive users

# Grand total of balances 

def add_balances():
    total = 0 
    for profile in profiles: 
        balance = profile["balance"]
        balance_without_commas = balance.replace(",", "")
        balance_without_dollarsign = balance_without_commas.replace("$", "")
        total = float(balance_without_dollarsign)
    return total

add_balances()
 


 # Average balance per user 

 user['balance'] for user in users


    



