from random import randint

# INITIAL VARIABLES
suits = ["hearts", "diamonds", "spades", "clubs"]  # ♥ ♦ ♣ ♠
cardsPerSuit = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cards = []

# GENERATE THE CARDS
for suit in suits:
    for card in cardsPerSuit:
        cards.append(suit + str(card))

"""
COMBINATIONS:
ROYAL FLUSH: STRAIGHT [10, A] OF THE SAME SUIT
STRAIGHT FLUSH: STRAIGHT WITH CARDS OF THE SAME SUIT
FOUR OF A KIND: 4 IDENTICAL CARDS
FULL HOUSE: A PAIR AND A THREE OF A KIND
FLUSH: 5 CARDS OF THE SAME SUIT
STRAIGHT: 5 CARDS WITH CONSECUTIVE NUMBERS
THREE OF A KIND: 3 IDENTICAL CARDS
TWO PAIR: 2 PAIRS
PAIR: 2 IDENTICAL CARDS
HIGH CARD: THE HIGHEST CARD
"""

# Declare classes
class playerClass:
    def __init__(self, name: str, chips: int):
        self.name = name  # A string with the player's name
        self.chips = chips  # An int with the chips (without counting the bet) of the player
        self.bet = None  # An int with the player's bet
        self.cards = []  # A list with the 2 cards given to the player
        self.playableCards = []  # A list with the cards in hand and the cards on the table
        self.bestHand = None  # Written as numbers, from 1 to 10

    def __str__(self):
        return f"The player {self.name} has {self.chips} chips."


class playableCardsClass:
    def __init__(self, cards: list):
        self.cards = cards
        self.suits = []
        for i in range(0, 7):
            self.suits.append(self.cards[i][:-1])  # Extract the suit from the card representation


class tableClass:
    def __init__(self, pot=0):
        self.pot = pot
        self.cards = []

class hands:
    @staticmethod
    def getSuits(cards):
        suits = [card[:-1] for card in cards]  # Extracts the suit from each card
        return suits

    @staticmethod
    def count(elements, minimum):
        counter = {}
        for element in elements:
            if element in counter:
                counter[element] += 1
            else:
                counter[element] = 1
        for element, quantity in counter.items():
            if quantity > minimum:
                return True
        return False

    @staticmethod
    def royalFlush(cards):
        suits = hands.getSuits(cards)
        return hands.count(suits, 5)  # This logic needs to be defined properly

players = []
table = tableClass()
numberOfPlayers = int(input("Number of players: "))
initialChips = int(input("Enter the initial amount of chips for each player: "))

# Deal cards
for i in range(numberOfPlayers):
    players.append(playerClass(input(f"Enter the name of player {i + 1}: "), initialChips))
    players[i].cards.append(cards.pop(randint(0, len(cards) - 1)))
    players[i].cards.append(cards.pop(randint(0, len(cards) - 1)))

for i in range(5):
    table.cards.append(cards.pop(randint(0, len(cards) - 1)))

for i in range(numberOfPlayers):
    players[i].playableCards = playableCardsClass(players[i].cards + table.cards)

# TODO: ADD ROUNDS, BETS, AND SO ON

# Check possible hands
for i in range(numberOfPlayers):
    if hands.royalFlush(players[i].playableCards.cards):
        players[i].bestHand = 10  # Assign a high rank if a royal flush is detected

# TODO: REMOVE LATER
for player in players:
    print(player)
print(cards)
