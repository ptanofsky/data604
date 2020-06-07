'''
Discussion #1
Author: Philip Tanofsky
Date: 06/02/2020

Prompt:
Write a simulation for  a simple game of chance
(e.g., drawing cards, rolling one or more dice, etc.)
Run the simulation 1000 times and interpret the outcome.
Post your code here, and discuss what might be done to improve it.  

'''
import random

def two_dice_sim(sim_count):

    # Initialize dictionary with valid results (2-12)
    results = {x: x*0 for x in range (2, 13)}
    # And with total count
    results['tot'] = 0

    # Run simulation
    for n in range(1, sim_count+1):

        die_01 = random.randint(1, 6)
        die_02 = random.randint(1, 6)
        dice_roll_total = die_01 + die_02

        # Increment result
        results[dice_roll_total] += 1
        # Increment total count
        results['tot'] += 1

    return results

def percentage_diff(results):
    # Expected percentages
    exp_pct = { 2: 2.78,  3:  5.56, 4:  8.33, 5: 11.11, 6: 13.89,
                7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78 }
    
    results_pct_diff = {x: x*0 for x in range (2, 13)}
    
    # Compare
    for n in range(2, len(results) + 1):
        results_pct_diff[n] = round((results[n] / results['tot'] * 100)
                                    - exp_pct[n], 2)

    return results_pct_diff


sim = two_dice_sim(1000)
print(sim)
print(percentage_diff(sim))


