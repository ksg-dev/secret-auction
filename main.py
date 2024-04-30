from art import logo
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

print(logo)
print("Welcome to the secret auction program.")

docket = {}
taking_bids = True


def bids(name, bid):
    docket[name] = bid

def winner():
    highest = 0
    winner = ""
    for person, bid in docket.items():
        if bid > highest:
            highest = bid
            winner = person
    print(f"The winner is {winner} with a bid of ${highest}")
    
        

while taking_bids:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids(name, bid)
    another = input("Are there any other bidders? Type 'yes' or 'no': ").lower().strip()
    if another == "no":
        taking_bids = False
        winner()
    else:
        clear()
    

print(docket)