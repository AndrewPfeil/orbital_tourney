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

It was necessary to invent my own tournament style for this league. The league has some apparently unique requirements that other tournament types do not meet. 
	Requirements:
-	Determine new seed based only on wins and losses (no ties allowed)
o	Rules out single elimination
-	Easy for participants to visualize and understand
o	Rules out swiss (cryptic ranking algorithms hide progress from players)
-	Keep the number of battles proportionally low
o	Rules out round robin
-	Don’t force players who know they’re doing poorly to keep battling without hope of winning
o	Rules out double elimination
-	Allow for fair underdog wins
Comprehensive testing is still underway, but having undergone proof of concept testing, it appears to work well. With that in mind, I present to you:
Orbital Tournaments
•	Participants are seeded in an orbital ring around “stardom”
•	Win “best 2/3” matches against neighbors on your ring to earn “gravity” 
•	Gravity moves you to an orbital ring closer to “stardom”
•	With 2 neighbors 
o	2 wins earns gravity
o	1 win, 1 loss maintains gravity
o	2 losses and you lose gravity
•	With 1 neighbor
o	1 win earns gravity
o	1 loss maintains gravity
•	The tournament ends when there is only one player on every orbital ring
•	The closer you are to “stardom”, the higher your rank 
