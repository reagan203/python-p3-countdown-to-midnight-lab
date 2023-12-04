# your code goes here!
# lib.py

import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        time.sleep(1)  # Pause for one second
        seconds -= 1
    print("HAPPY NEW YEAR!")
