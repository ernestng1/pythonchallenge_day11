from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_or_one(total):
    """Function that determines whether ace is 1 or 11 in value based on total value of cards"""
    if total > 21:
        return 1
    else:
        return 11

def draw_card_player(deck):
    """Player draws a card and if the resultant sum is less than or equal to 21, returns True. Otherwise,
    false which means player loses"""
    card_to_pick = random.choice(cards)
    if card_to_pick == 11:
        card_to_pick = ace_or_one(sum(deck)+11)
    deck.append(card_to_pick)
    if sum(deck) <= 21:
        return True, deck
    else:
        return False, deck

def draw_card_computer(deck):
    """Computer draws a card and if the resultant sum is less than or equal to 21, returns True. Otherwise,
    false which means player loses"""
    card_to_pick = random.choice(cards)
    if card_to_pick == 11:
        card_to_pick = ace_or_one(sum(deck) + 11)
    deck.append(card_to_pick)
    if sum(deck) < 17:
        return draw_card_computer(deck)
    elif sum(deck) > 17 and sum(deck) <= 21:
        return True, deck
    else:
        return False, deck

def initiate_deck():
    """Function to randomly assign cards to deck"""
    deck = []
    for i in range(2):
        deck.append(random.choice(cards))
    if sum(deck) == 22:
        '''Case where you get double ace'''
        deck = random.choice([[11, 1],[1,11],[1,1]])
    return deck

def result(player_deck, computer_deck, game_result):
    """Function to establish results of the blackjack game"""
    print(f"Your final cards: {player_deck}, final score: {sum(player_deck)}")
    print(f"Computer's final cards: {computer_deck}, final score: {sum(computer_deck)}")
    if game_result == "lose":
        print("You lose!")
    elif game_result == "win":
        print("You win!")
    elif game_result == "draw":
        print("A Draw!")
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack()

def blackjack():
    """Blackjack game"""
    print(logo)
    player_deck = initiate_deck()
    computer_deck = initiate_deck()
    collect_card = True
    print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"Computer's first card: {computer_deck[0]}")
    while collect_card == True:
        player_wish = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_wish == "y":
            player_result, player_deck = draw_card_player(player_deck)
            if player_result == False:
                collect_card = False
            else:
                print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
        elif player_wish == "n":
            player_result = True
            collect_card = False

    if player_result == False:
        result(player_deck, computer_deck, "lose")

    else:
        computer_result, computer_deck = draw_card_computer(computer_deck)
        if computer_result == False:
            result(player_deck, computer_deck, "win")
        else:
            if sum(player_deck) > sum(computer_deck):
                result(player_deck, computer_deck, "win")
            elif sum(player_deck) < sum(computer_deck):
                result(player_deck, computer_deck, "lose")
            elif sum(player_deck) == sum(computer_deck):
                result(player_deck, computer_deck, "draw")

blackjack()