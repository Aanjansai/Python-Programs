"""  Desc -> Simulates a gambler who start with $stake and place fair $1 bets until he/she goes
     broke (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number of bets
     he/she makes. Run the experiment N times, averages the results, and prints them out.
     I/P -> $Stake, $Goal and Number of times
     Logic -> Play till the gambler is broke or has won
     O/P -> Print Number of Wins and Percentage of Win and Loss."""

from UtilityMethods import Utility
try:
    stake = int(input("enter the stake value \n"))
    goals = int(input("enter the goals \n"))
    trails = int(input("enter the number of trails \n"))
    Utility.gambler_method(stake, goals, trails)
except Exception as e:
    print(e)
    print("enter integer value ")
    
