"""
This python code is a game of blackjack using CLI for input.
The computer is referred to as the "dealer" or "house".
The user is referred to as the "player".
"""

from random import choice as ch #Random is used for picking the cards of the player and dealer.

#Define functions
#Asks the user if they want to play again
def PlayAgain():
    restart = False
    
    #Use a conditioned while loop to check if the user wants to play again.
    while restart == False:
        again = stringInput("\nWould you like to play again?")
        again = again.lower()
        if again == "yes" or again == 'y':
            return True
        elif again == "no" or again == 'n':
            return False
        else:
            print("\nPlease enter yes or no.")
        #end if
    #end while
#end def

#Function to randomly pick a card
def NewCard():
    global deck
    card = ch(deck)
    return card
#end def

#Function to get the user's desicion
def Choice():
    global PTotal, playerDeck, deck, CardValues, DTotal, PScore, HScore
    
    run = False
    
    #Use a conditioned while loop to ask if the user wants to hit or stand
    while run != True:
        choice = stringInput("Hit or Stand?")
        choice = choice.lower()
        if choice == "hit":
            Card = (NewCard())
            playerDeck.append(Card)
            PTotal = Calculate(playerDeck, PTotal)
            print(f"\nThe value of your cards is {PTotal} and your cards are {', '.join(playerDeck)}.")
            Check = ValueCheck()
            if Check == True:
                run = True
            
        elif choice == "stand":
            run = True
        else:
            print("\nPlease pick hit or stand.")
        #end if
    #end while
#end def

#Fuction to make the hand of all players
def CreateHand():
    global deck
    
    decks = []
    i = 1
    
    #Use a for loop to only give 2 cards to the hand.
    for i in range(2):
        card = NewCard()
        decks.append(card)
        i += 1
    #end for
    return decks
#end def

#Function to caculate the value of the cards given to the player and dealer
def Calculate(hand, total):
    global CardValues
    total = 0
    aces = []

    #use a for loop to go through the whole deck to caulate the value of the deck
    for card in hand:
        rank = card.split(" ")[0]
        total += CardValues[rank]
        if rank == "Ace" or rank == 'ace':
            aces.append(card)
        #end if
    #end for

    #Use a while loop to make an ace worth one if the total value has gone over 21
    for i in aces:
        while total > 21:
            for card in aces:
                total -= 10
                aces.pop()
    #end while

    return total
#end def

#A function to check if the dealer or player has gone bust.
def ValueCheck():
    global PTotal, DTotal, PScore, HScore, Bust
    
    if PTotal == 21 and DTotal == 21:
        print("\nYou have both gone bust.\nThis game is a draw.")
        HScore += 1
        PScore += 1
        Bust = True
        return True
            
    elif PTotal > 21:
        print("\nYou have gone bust.\nHouse Wins")
        HScore += 1
        DisplayScores()
        Bust = True
        return True
        
    elif DTotal > 21:
        print("\nDealer has gone bust.\nYou Win.")
        PScore += 1
        DisplayScores()
        Bust = True
        return True
    
    elif DTotal == 21:
        print("\nThe dealer has won with blackjack.")
        HScore += 1
        DisplayScores()
        Bust = True
        return True
    
    elif PTotal == 21:
        print("\nYou have won with blackjack.")
        PScore += 1
        DisplayScores()
        Bust = True
        return True
    else:
        return False
        #end if
    #end while
#end def

#A function to see who has the highest score
def TotalCheck():
    global PTotal, DTotal, PScore, HScore
    check = False
    
    while check != True:
        if PTotal > DTotal:
            print("\nYou Win.")
            PScore += 1
            DisplayScores()
            check = True
            
        elif PTotal < DTotal:
            print("\nHouse Wins.")
            HScore += 1
            DisplayScores()
            check = True
        
        elif PTotal == DTotal:
            print("\nThe game is a draw.")
            HScore += 1
            PScore += 1
            check = True
            
        else:
            print("\nAn error has occured.")
        #end if
    #end while
#end def

#A function for the computer to decide wether to "hit" or "stand".
def DelearChoice():
    global DTotal, dealerHand, deck, CardValues, PTotal, PScore, HScore
    run = True
    
    while run == True:
        if DTotal >= 17:
            return DTotal, dealerHand
            run = False
        elif DTotal <= 16:
            Card = (NewCard())
            dealerHand.append(Card)
            DTotal = Calculate(dealerHand, PTotal)
            if ValueCheck() == True:
                run = True
        #end if
    #end while
#end def

#Made a function to correctly display game or games depeding on the score of the player and computer (House/Delear)
def DisplayScores():
    global PScore, HScore
    if PScore > 1:
        if HScore > 1:
            print(f"\nGame has ended you have won {PScore} games.\nThe computer has won {HScore} games.")
        elif HScore <= 1:
            print(f"\nGame has ended you have won {PScore} games.\nThe computer has won {HScore} game.")
        #end if
    elif PScore <= 1:
        if HScore <= 1:
            print(f"\nGame has ended you have won {PScore} game.\nThe computer has won {HScore} game.")
        elif HScore > 1:
            print(f"\nGame has ended you have won {PScore} game.\nThe computer has won {HScore} games.")
        #end if
    #end if
#end def

#Take a sting input and perform a presence check
def stringInput(reason):
    valid = False
    
    while valid != True:
        Input = input(f'{reason}: ')
        
        if Input == '':
            print("\nPlease do not leave the input blank.")
        else:
            return Input
        #end if
    #end while
#end def

#Make a deck of cards
def Deck(Cards):
    formed = False
    
    deck =[]
    i = 0
    x = 0
    for i in range(3):
        for x in range(11):
            Card = str(Cards[2][x])
            card = (Card.capitalize() + ' of ' + Cards[0][i].capitalize())
            deck.append(card)
        #end for
    #end for

    return deck
# end def

#Declare constants
CardValues = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'Ace' : 11,
  'Jack': 10,
  'King': 10,
  'Queen': 10
}

#Declare variables.
#The starting deck of cards
Cards = [
  #   0         1          2          3
  ["clubs", "diamonds", "hearts", "spades"],
  #  0        1
  ["red", "black"],
  #  0    1  2  3  4  5  6  7  8    9       10      11
  ["ace", 2, 3, 4, 5, 6, 7, 8, 9, "jack", "king", "queen"]
]

deck = Deck(Cards)
#Variables to keep track of who has won the most games.
PScore = 0
HScore = 0

#A variable to check if the game should keep running
Run = True

#Explain the game.
print("\nThis is a game of Blackjack.\nYou are the player and the computer is the delear and house.")

while Run == True:
    #A varibale to help with if statments below
    gameRun = True
    
    #A varibale to track if someone has gone bust
    Bust = False
    
    #Make the hands of the player and dealer.
    playerDeck = []
    dealerHand = []
    playerDeck = CreateHand()
    dealerHand = CreateHand()

    #Calculate the values of the player and dealer decks.
    PTotal = 0
    DTotal = 0
    PTotal = Calculate(playerDeck, PTotal)
    DTotal = Calculate(dealerHand, DTotal)
    
    #Show the cards
    print(f"\nOne of the dealers cards is {dealerHand[0]}.\nThe value of your cards is {PTotal} and your cards are {' and '.join(playerDeck)}.")
    
    check = ValueCheck()

    if check == False and gameRun == True:
            Choice()
            if Bust == False:
                DelearChoice()
                TotalCheck()
            gameRun = False
    if check == True or gameRun == False:
            choice = PlayAgain()
            if choice == False:
                Run = False
            elif choice == True:
                continue
            else:
                print("\nAn error has occured.")
    else:
            print("\nAn error has occured.")
    #end if
#end while

DisplayScores()
