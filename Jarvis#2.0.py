from jokes import jokebot
import travel
import time


def add(num1, num2):
    output = num1 + num2
    return output


def subtract(num1, num2):
    output = num1 - num2
    return output


def multiply(num1, num2):
    output = num1 * num2
    return output


def divide(num1, num2):
    output = num1 / num2
    return output


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
        out = jokebot(type)
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

            if (start == end):
                print(" you thought of ", end)
                break
            ans = input(' is your num greater than ' + str(mid) + " : ")

            if (ans == "y"):
                start = mid + 1
            else:
                end = mid
            mid = (int)((start + end) / 2)
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
