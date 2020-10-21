# orbital_tourney
Simulation and analysis of novel orbital tourney type

## Purpose
This tournament structure is being developed as an option for organizers who want the tournament to result in a complete 
ranking of participants based on wins and losses alone. 

The structure needs to be tested to determine if it allows for infinite competition loops and to determine if the number of games per player 
is reasonable for the number of competitors.

This structure also needs to be easy for users to understand and easy for organizers to use. Swiss tournaments and other styles exist that 
could acheive the same or similar goals, but are too complex for users to determine how they are doing midway, and too difficult to implement
due to ranking algorithms.

## Test Cases

The structure needs to be evaluated under the following parameters
* even vs. odd number of participants
* seed organization around start ring
* outcome probabilities (100% -> 0% seed accuracy)