import random

money = 100


#Write your game of chance functions here

def coinFlip(guess, bet):
    global money

    if bet <= 0 or bet > money :
        print("bet a positive value that you can afford!")
        return 0
    
    num = random.randint(0,1)

#win
    if num == 0 and guess == "Tails" or num == 1 and guess == "Heads":
        money += bet
        # print(" ")
        print(" !!! You WIN " + str(bet) + " with the guess " + guess + " you have the total of " + str(money) + "  !!! " )
        # print(" ")
        return money
#loose
    else:
        money -= bet
        # print(" ")
        print("You LOST " + str(bet) + " with the guess " + guess + " you have the total of " + str(money) )
        # print(" ")
        return money


def chohan(guess, bet):
    global money

    if bet <= 0 or bet > money :
        print("bet a positive value that you can afford!")
        return 0
    
    diceOne = random.randint(1,6)
    diceTwo = random.randint(1,6)

    result = diceOne + diceTwo

    if result % 2 == 0 and guess == "Even" or result % 2 != 0 and guess == "Odd":
        money += bet
        print(" !!! You WIN " + str(bet) + " with the guess " + guess + " you have the total of " + str(money) + "  !!! " )
    else:
        money -= bet
        print("You LOSE " + str(bet) + " with the guess " + guess + " you have the total of " + str(money) )
  
import itertools

def pickCard(bet):
    global money
    global cardname
    deck = list(itertools.product(range(2,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)

    for i in range(1):
        value1 = deck[i][0]
        suits1 = deck[i][1]     

    deck.pop(0)
    random.shuffle(deck)

    for i in range(1):
        value2 = deck[i][0]
        suits2 = deck[i][1]   

   
    
    if value1 < 11:
        cardname =  str(value1)
    elif value1 == 11 or value2 == 11:
        cardname = "Jack"
    elif value1 == 12 or value2 == 12:
        cardname = "Queens"
    elif value1 == 13 or value2 == 13:
        cardname = "King"
    elif value1 == 14 or value2 == 14:
        cardname = "Ace"
    
    print("You: " + cardname + " of "  + suits1)
    print("Computer:",value2, "of", suits2)

    if value1 == value2:
        print("Nobody wins")
        return 0
    
    if value1 > value2:
        money += bet
        print(" !!! You WIN " + str(bet) + ". You have the total of " + str(money) + "  !!! " )

    else:
        money -= bet
        print("Computer wins, you lost " + str(bet) + ". You have the total of " + str(money))
    


#Call your game of chance functions here
print(" ")
print(" Coin Flip ")
print(" ")

coinFlip("Tails", -10)
coinFlip("Tails", 200)
coinFlip("Tails", 10)
coinFlip("Tails", 20)
coinFlip("Tails", 30)

print(" ")
print(" Chohan ")
print(" ")

chohan('Odd', 10)
chohan('Odd', 20)
chohan('Odd', 100)

print(" ")
print(" Pick a Card ")
print(" ")

pickCard(2)