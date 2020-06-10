#Teletype printer

import time
import random

time_delay = 0.08
string_to_print = "Hello World! This program is a teletype printer. It looks cool, but that's pretty much all it's good for. :D"

def teletype_print(what_to_print):
    for ch in what_to_print:
        print(ch, end = "")
        if (ch == " "):
            time.sleep(3*time_delay)
        else:
            time.sleep(time_delay + random.randint(0,10)/100.0)
    print()

teletype_print(string_to_print)

user_input = input("Enter some text to teletype: ")

teletype_print(user_input)