import random


################################################################################
# shuffle
# return a new "shuffled deck" of 52 cards
################################################################################

def shuffle():
    count = 0
    new_deck = []
    # populate the deck with numbers 0-12 4 times for the different cards
    while count < 52:
        new_deck.insert(count, int(count % 13))
        # print(count)
        # print(count % 13)
        # print()
        count = count + 1
    # shuffle the deck
    random.shuffle(new_deck)
    # print entire deck and display number of each card
    """while(testCount < 52):
        print("Card " + str(testCount+1) + ": " + str(newDeck[testCount]))
        testCount = testCount + 1
    print("Number of Aces: " + str(newDeck.count(0)))
    print("Number of Twos: " + str(newDeck.count(1)))
    print("Number of Threes: " + str(newDeck.count(2)))
    print("Number of Fours: " + str(newDeck.count(3)))
    print("Number of Fives: " + str(newDeck.count(4)))
    print("Number of Sixes: " + str(newDeck.count(5)))
    print("Number of Sevens: " + str(newDeck.count(5)))
    print("Number of Eights: " + str(newDeck.count(6)))
    print("Number of Nines: " + str(newDeck.count(7)))
    print("Number of Tens: " + str(newDeck.count(8)))
    print("Number of Jacks: " + str(newDeck.count(9)))
    print("Number of Queens: " + str(newDeck.count(10)))
    print("Number of Kings: " + str(newDeck.count(11)))"""
    return new_deck


###############################################################################
# is_winner
# determine if the user won the game. hand_one for user, hand_two for dealer
###############################################################################
def is_winner(hand_one, hand_two, score_hand_one, score_hand_two):
    print("You have " + str(len(hand_one)) + " cards and your score is: " + str(score_hand_one))
    print("The dealer has " + str(len(hand_two)) + " cards and their score is: " + str(score_hand_two))
    # user has a five card charlie
    if (len(hand_one) == 5) and (score_hand_one < 22):
        print("You win!")
    # user has beaten the dealer
    elif (score_hand_one > score_hand_two) and (score_hand_one < 22):
        print("You win!")
    elif (score_hand_one < 22) and (score_hand_two > 21):
        print("You win!")
    # no one wins
    elif (score_hand_one > 21) and (score_hand_two > 21):
        print("You both lose!")
    # dealer wins
    else:
        print("You lose!")


#################################################################################
# score
# count the score of a hand of cards
# returns the score
#################################################################################
def score(hand, in_aces):
    this_score = 0
    count = 0
    size_of_hand = len(hand)
    aces = in_aces
    while count < size_of_hand:
        # current card is a jack, queen, or king
        if (hand[count] == 10) or (hand[count] == 11) or (hand[count] == 12):
            this_score = this_score + 10
        elif hand[count] == 0:
            this_score = this_score + 11
        else:
            this_score = this_score + hand[count] + 1
        count = count + 1
    if this_score > 21:
        while aces > 0:
            this_score = this_score - 10
            aces = aces - 1
            print("Your ace counts as a 1")
    return this_score


#############################################################################
# what_card
# convert the int card number received to the str card name
# returns the string version of the card number
#############################################################################
def what_card(in_card):
    if in_card == 0:
        return "Ace"
    if in_card == 1:
        return "Two"
    if in_card == 2:
        return "Three"
    if in_card == 3:
        return "Four"
    if in_card == 4:
        return "Five"
    if in_card == 5:
        return "Six"
    if in_card == 6:
        return "Seven"
    if in_card == 7:
        return "Eight"
    if in_card == 8:
        return "Nine"
    if in_card == 9:
        return "Ten"
    if in_card == 10:
        return "Jack"
    if in_card == 11:
        return "Queen"
    if in_card == 12:
        return "King"


#########################################################################
# Black Jack Main
# plays a game of black jack
########################################################################
print("Welcome to Black Jack!")
print("In this game, enter \"h\" to hit and \"s\" to hold.\n")
keep_playing = True

while keep_playing:

    print("Shuffling deck...")

    # create useful parameters
    dealer_move = "h"
    deck = shuffle()
    num_turn = 2
    user_deck = []
    dealer_deck = []
    user_aces_one = 0
    user_aces_eleven = 0
    dealer_aces_one = 0
    dealer_aces_eleven = 0

    print("Dealing the dealer's hand...")
    # dealers first turn
    dealer_deck.insert(0, deck[0])
    deck.pop(0)
    dealer_deck.insert(1, deck[0])
    deck.pop(0)
    dealer_aces = dealer_deck.count(0)
    dealer_score = score(dealer_deck, dealer_aces)

    print("Dealing your hand...")
    # users first turn
    user_deck.insert(0, deck[0])
    # insert an ace into the users deck for testing
    # userDeck.insert(0, 0)
    deck.pop(0)
    user_deck.insert(1, deck[0])
    # insert an ace into the users deck for testing
    # userDeck.insert(1, 0)
    deck.pop(0)
    user_aces = user_deck.count(0)
    user_score = score(user_deck, user_aces)

    print("Look at the table...")

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    print("The dealer has a " + what_card(dealer_deck[0]))
    print("The dealer has 2 cards.\n")
    # display the dealers cards for testing
    # print("The dealer has a " + whatCard(dealerDeck[0]) + " and a " + whatCard(dealerDeck[1]))

    print("You have a " + what_card(user_deck[0]) + " and a " + what_card(user_deck[1]))
    print("You have 2 cards.")
    print("Your score is: " + str(user_score))

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    print("Time to play...")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    user_move = input("Would you like to hit or hold? ")

    # while the user wishes to hit
    while (user_move == "h") or (dealer_move == "h"):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if user_move == "h":
            # users turn
            # insert a 1 into the users deck for testing
            # userDeck.insert(numTurn, 1)
            # draw a card and remove one from the deck
            user_deck.insert(num_turn, deck[0])
            deck.pop(0)
            user_aces = user_deck.count(0)
            # show the user what they drew
            print("You have drawn a: " + what_card(user_deck[num_turn]))
            user_score = score(user_deck, user_aces)
            print("Your score is: " + str(user_score))
            print("You have " + str(len(user_deck)) + " cards.\n")
            if user_score > 21:
                user_move = "S"
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if dealer_move == "h":
            # dealers turn. stop hitting at 17
            if dealer_score < 17:
                dealer_deck.insert(num_turn, deck[0])
                deck.pop(0)
                dealer_aces = dealer_deck.count(0)
                dealer_score = score(dealer_deck, dealer_aces)
                print("The dealer hits.")
                print("The dealer has " + str(len(dealer_deck)) + " cards.\n")
            else:
                print("The dealer holds.")
                dealer_move = "s"
        num_turn = num_turn + 1
        # check to see if the user got a five card charlie
        if (user_score < 22) and (num_turn == 5):
            break
        # ask the user if they want another card if they haven't lost yet
        elif (user_score < 22) and (user_move == "h"):
            user_move = input("Would you like to hit or hold? ")
        print()
    # user said hold. see if the user won or lost
    is_winner(user_deck, dealer_deck, user_score, dealer_score)

    keep_playing_ans = input("Would you like to continue? (y/n)")
    if (keep_playing_ans == "y") or (keep_playing_ans == "Y"):
        keep_playing = True
    else:
        keep_playing = False
