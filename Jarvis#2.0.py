from datetime import datetime

flight_locations = ["Delhi", "Chennai", "Mumbai", "Kolkatta", "Hyderabad", "New York", "Sydney", "Beijing", "Berlin",
                    "San Fransisco"]
flight_times = [100, 300, 530, 1200, 1530, 1700, 1930, 2130, 2230]

train_locations = ["Delhi", "Chennai", "Mumbai", "Kolkata", "Lahore", "Karachi", "Dhaka", "Patna", "Pune", "Hyderabad",
                   "Darjeeling"]

now = 0


def flightsearch(location):
    if location in flight_locations:
        now = datetime.now()
        current_time = now.strftime("%H%M")
        current_time = int(current_time)
        for flightime in flight_times:
            if (flightime > current_time):
                next_flight = str(flightime)
                current_time = str(current_time)
                response = "The current time is " + current_time + ", and the next flight to " + location + " takes off at " + next_flight + " and costs Rs.5000."
                return (response)
                break
    else:
        response = "Sorry, there aren't any flights to " + location + " at this moment."
        return (response)


def trainsearch(location):
    if location in train_locations:
        if location in flight_locations:
            return ("There is a train to " + location + ". I would suggest you to book a flight.")
        else:
            return ("There is a train to " + location + ", and it departs at every hour and costs Rs.2000.")
    else:
        return ("Sorry,No trains to " + location + " at this point.")


import random

knock_knock = [
    "Knock knock. Who’s there? Cow says. Cow says who? No, a cow says mooooo!",
    "Knock knock. Who’s there? A little old lady. A little old lady who? All this time, I had no idea you could yodel.",
    "Knock knock. Who’s there? Tank. Tank who? You’re welcome.",
    "Knock Knock. Who’s there? Voodoo. Voodoo who? Voodoo you think you are, asking all these questions?",
    "Knock, Knock. Who’s there? Nobel. Nobel who? Nobel, that’s why I knocked!"
    "Knock, knock. Who’s there? Luke. Luke who? Luke through the peep hole and find out."
]

riddle_dict = {
    "I’m tall when I’m young, and I’m short when I’m old. What am I? ": "candle",
    "What month of the year has 28 days? ": "All of them",
    "What question can you never answer yes to?": "are you sleeping",
    "I am in school and home.I have a mouse. You can use me for work. You can use me for email. What am I? ": "computer"
}


def joke_bot(type):
    if type == "Knock Knock" or type == "knock knock":
        jokenum = random.randint(0, 3)
        out = knock_knock[jokenum]
        return (out)
    elif type == "Riddle" or type == "riddle":
        riddle, answer = random.choice(list(riddle_dict.items()))
        r = input(riddle)
        if r == answer:
            return "You got it correct"
        else:
            return "You got it wrong the correct answer is" + answer


from jokes import joke_bot
import travel
import time
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

name = input("Hello, I am your virtual assistant. What is your name?: ")
print("Hello ", name, ", I am Jarvis 2.0.")

time.sleep(1.0)

while True:
    opt = input("""
    To search for flights, type in 'F': 
    To search for Trains, type in 'T'. :
    To hear a joke, type in 'J', :
    To calculate, type 'C'. :
    To send a Email, type 'E':   
    To play guess the number, type 'G':
    To open Palindrome checker, type 'P' 
    To quit, type 'Q':\n
    """)

    if opt == "F" or opt == "f":
        location = input("Where do you want to fly to?: ")
        out = travel.flightsearch(location)
        print(out)
        time.sleep(1.0)
    elif opt == "T" or opt == "t":
        location = input("Where do you want to travel to?: ")
        out = travel.trainsearch(location)
        print(out)
        time.sleep(1.0)
    elif opt == "J" or opt == "j":
        type = input("Do you want to hear a 'Riddle' or a 'Knock Knock'?: ")
        out = joke_bot(type)
        print(out)
        time.sleep(1.0)
    elif opt == "E" or opt == "e":
        to = input("To: ")
        subject = input("Subject: ")
        email = input(""" Email: 
""")
        print(f"Sending to {to}.......")
        time.sleep(1.5)
        print(f"Sent {subject} to {to}")
        time.sleep(1.0)
    elif opt == "P" or opt == "p":
        print("I am the PALINDROME checker")
        p = input('Enter a any word or number and I will tell if it is a palindrome:\n')

        mid = int(len(p) / 2)
        for x in range(mid):
            if p[x] != p[- (x + 1)]:
                print("This is not a palindrome.")
                exit(0)

        print("It is a palindrome")

    elif opt == "G" or opt == "g":
        start = 1
        end = 1000
        mid = (int)((start + end) / 2)
        print("think of num from 1 to 1000")
        print(mid)
        while (True):

            if start == end:
                print(" you thought of ", end)
                break
            ans = input(' is your num greater than ' + str(mid) + " : ")

            if ans == "y":
                start = mid + 1
            else:
                end = mid
            mid = int((start + end) / 2)
        time.sleep(1.0)
    elif opt == "C" or opt == "c":
        num1 = int(input("Input number one :  "))
        num2 = int(input("Input number two :  "))
        operator = input("To add, press'+'. To subtract, press '-'. To multiply, press '*'. To divide, press'/':  ")

        if operator == "+":
            ans = add(num1, num2)
        elif operator == "-":
            ans = subtract(num1, num2)
        elif operator == "*":
            ans = multiply(num1, num2)
        elif operator == "/":
            ans = divide(num1, num2)
        else:
            ans = "invalid input"
        print("your answer is:", ans)
        time.sleep(1.0)
    elif opt == "Q" or opt == "q":
        print(f"Bye {name}")
        break
    else:
        out = "Input a valid command."
        print(out)
        time.sleep(1.0)
