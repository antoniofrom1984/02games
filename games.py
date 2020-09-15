import random

money = 100


#Write your game of chance functions here

def coinFlip(guess, bet):
    global money
    #make sure is the required spealing
    if type(guess) == str:
        if guess != "Tails" and guess != "Heads": 
            print("Please mind spealing 'Tails' or 'Heads'")
            print(" ")
            return 
    #check if you using a number for you bet
    if type(bet) != int and type(bet) != float:
        print("Please use a number for your bet")
        print(" ")
        return 
    if bet <= 0 or bet > money :
        print("bet a positive value that you can afford!")
        return 0
    
    num = random.randint(0,1)

#win
    if num == 0 and guess == "Tails" or num == 1 and guess == "Heads":
        money += bet
        # print(" ")
        print("!!! You WIN " + str(bet) + "£ with the guess " + guess + " you have the total of " + str(money) + "£.  !!!" )
        # print(" ")
        return money
#loose
    else:
        money -= bet
        # print(" ")
        print("You LOST " + str(bet) + "£ with the guess " + guess + " you have the total of " + str(money)+ "£." )
        # print(" ")
        return money


def chohan(guess, bet):
    global money

    #make sure is the required spealing
    if type(guess) == str:
        if guess != "Even" and guess != "Odd": 
            print("Please mind spealing 'Even' or 'Odd'")
            print(" ")
            return 
    #check if you can afford the bet
    if bet <= 0 or bet > money :
        print("bet a positive value that you can afford!")
        return 0
    
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)

    result = diceOne + diceTwo

    if result % 2 == 0 and guess == "Even" or result % 2 != 0 and guess == "Odd":
        money += bet
        print("!!! You WIN " + str(bet) + "£ with the guess " + guess + " you have the total of " + str(money) + "£  !!!" )
    else:
        money -= bet
        print("You LOSE " + str(bet) + "£ with the guess " + guess + " you have the total of " + str(money)+ "£." )
  
# import itertools
from itertools import product

def pickCard(bet):
    global money
    #create deck
    deck = list(product(range(2,14),['Spade','Heart','Diamond','Club']))
    #shuffle deck
    random.shuffle(deck)
    #choose the first card of shuffled deck, player
    for i in range(1):
        value1 = deck[i][0]
        suits1 = deck[i][1]     
    #remove card from deck
    deck.pop(0)
    #shuffle for computer player
    random.shuffle(deck)

    for i in range(1):
        value2 = deck[i][0]
        suits2 = deck[i][1]   
    
    # print(deck)
    
    print("You: " + cardValues(value1) + " of "  + suits1)
    print("Computer: " + cardValues(value2) + " of "  + suits2)

    if value1 == value2:
        print("Nobody wins")
        return 0
    
    if value1 > value2:
        money += bet
        print("!!! You WIN " + str(bet) + "£. You have the total of " + str(money) + "$  !!!" )

    else:
        money -= bet
        print("Computer wins, you lost " + str(bet) + "£. You have the total of " + str(money)+ "£.")

#helper function to give names to the cards
def cardValues(num):
    if num < 11:
        return str(num)
    if num == 11:
        return "Jack"
    if num == 12:
        return "Queens"
    if num == 13:
        return "King"
    if num == 14:
        return "Ace"

def roulette(guess, bet):
    global money
    
    #rolette numbers in the right order
    roulette = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
    
    #choose random 
    pick = random.choice(roulette)

    #make sure is the required spealing
    if type(guess) == str:
        if guess != "Even" and guess != "Odd": 
            print("Please mind spealing 'Even' or 'Odd'")
            print(" ")
            return 
    
    #declare the random number        
    print("The wheel landed on " + str(pick) + ". Your guess is " + str(guess))

    #check if you can afford it
    if bet <= 0 or bet > money :
        print("bet a positive value that you can afford!")
        return None
    
    #check if it fell in 0 or 00 position
    elif pick == roulette[19] or  pick == roulette[0]:
        money -= bet
        print("you LOSE " + str(bet) +"£! landed on 0 or 00! You have the total of "  + str(money)+ "£.")
        print(" ")
        return None
    
    elif pick % 2 == 0 and guess == "Even" or pick % 2 != 0 and guess == "Odd":
        money += bet
        print("You Win "+ str(bet) +"£! You have the total of "  + str(money)+ "£.")
        print(" ")
        return None
    elif guess == pick:
        money += bet * 35
        print("You Win "+ str(bet*35) +"£! You have the total of "  + str(money)+ "£.")
        print(" ")
        return 

    else:
        print("you LOSE " + str(bet) +"£!! You have the total of "  + str(money)+ "£.")
        print(" ")




#Call your game of chance functions here
print(" ")
print(" Coin Flip ")
print(" ")

coinFlip("Tails", -10)
coinFlip("Tails", 200)
coinFlip("Tails", 10)
coinFlip("Tails", 20)
coinFlip("Heads", 30)
coinFlip("Heads  ", 2)
coinFlip("Heads", "money")

print(" ")
print(" Chohan ")
print(" ")

chohan('Odd', 10)
chohan('Odd', 20)
chohan('Odd', 100)

print(" ")
print(" Pick a Card, any card! ")
print(" ")

pickCard(2)

print(" ")
print(" Roulette! ")
print(" ")

roulette("Even", 2)
roulette("Odd", 2)
roulette("Odds", 2)
roulette("Odd  ", 2)
roulette(27, 2)

