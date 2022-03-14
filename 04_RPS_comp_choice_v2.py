# RPS Component 1 - generator computer choice

import random

rps_list = ["rock", "paper", "scissors", "xxx"]

for item in range(0,20):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")