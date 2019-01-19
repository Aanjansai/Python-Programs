""" Desc -> Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
    I/P -> Start the Stopwatch and End the Stopwatch
    Logic -> Measure the elapsed time between start and end
    O/P -> Print the elapsed time."""


from UtilityMethods import Utility

try:
    a = int(input("Press 0 to start the time "))
    b = int(input("Press 1 to Stop the time "))
    Utility.start1()
    Utility.stop1()
    Utility.elapsed_time()

except ValueError:
    print("Invalid Input")

