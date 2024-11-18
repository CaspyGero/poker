from random import randint
#INITIAL VARIABLES
suits = ["hearts", "diamonds", "spades", "clubs"] #♥ ♦ ♣ ♠
symbolsPerSuit = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cards = []
#TODO: MAY BE TOO COMPLICATED, CONFIRM LATER
class cardClass:
    def assignValue(symbol):
        values = {
            "2" : 1,
            "3" : 2,
            "4" : 3,
            "5" : 4,
            "6" : 5,
            "7" : 6,
            "8" : 7,
            "9" : 8,
            "10" : 9,
            "J" : 10,
            "Q" : 11,
            "K" : 12,
            "A" : 13,
        }
        return values[symbol]
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol
        self.value = cardClass.assignValue(symbol)
    def __str__(self):
        return suit + str(self.symbol)
    def __add__(self, other):
        if isinstance(other, cardClass):
            return cardClass(self.suit + other.suit, self.symbol + other.symbol)
        elif isinstance(other, tableClass):
            return cardClass(self.suit + other.cards.suit, self.symbol + other.cards.symbol) #Looks weird but makes logic
        else:
            raise TypeError("Cannot add CardClass object with non-CardClass or non-tableClass object")
#GENERATE THE CARDS
for suit in suits:
    for symbol in symbolsPerSuit:
        cards.append(cardClass(suit, str(symbol)))
"""
TODO: REMOVE LATER
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
#DECLARE CLASSES
class playerClass:
    def __init__(self, name: str, chips: int):
        self.name = name  # A string with the player's name
        self.chips = chips  # An int with the chips (without counting the bet) of the player
        self.bet = None  # An int with the player's bet
        self.cards = []  # A list with the 2 cards given to the player
        self.playableCards = []  # A list with the cards in hand and the cards on the table
        self.bestHand = None  # Written as a tuple of numbers, from 1 to 10, in the form of (type value, symbol value)
    def __str__(self):
        return f"The player {self.name} has {self.chips} chips."
class playableCardsClass:
    def __init__(self, suit, symbol):
        self.suits = suit
        self.symbols = symbol
class tableClass:
    def __init__(self, pot=0):
        self.pot = pot
        self.cards = []
class hands:
    def getPermutations(base: list) -> list:
        if len(base) == 1:
            return [base]
        permutations = []
        for i in range(len(base)):
            actualIndex = [base[i]]
            resto = base[:i] + base[i+1:]
            for p in hands.getPermutations(resto):
                permutations.append(actualIndex + p)
        return permutations
    def sublistCoincidence(list1, list2):
        setList1 = {tuple(sublist) for sublist in list1}
        setList2 = {tuple(sublist) for sublist in list2}
        return bool(setList1 & setList2)
    #TODO: ONLY SAYS IF THE COUNT IS CORRECT, SHOULD RETURN A DICTIONARY WITH THE COUNT OF EVERY ELEMENT
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
    #I will use a lot: bool(set(lista1) & set(lista2))
    def flush(cards):
        #TODO: CHECK IF IT WORKS, IT SHOULD
        if(str(cards) in (str(symbolsPerSuit) + str(symbolsPerSuit))):
            return True
    def royalFlush(suits, symbols):
        #FIXME: DOESNT WORK AS EXPECTED, DOESNT CHECK IF THEY HAVE THE SAME SUIT
        suits = suits
        royal = [["10", "J", "Q", "K", "A"]] #Sublist with the only possible royal flush
        if hands.count(suits, 5):
            return hands.sublistCoincidence(hands.getPermutations(symbols), royal)
players = []
table = tableClass()
numberOfPlayers = int(input("Number of players: "))
initialChips = int(input("Enter the initial amount of chips for each player: "))
#DEAL CARDS
for i in range(5):
    table.cards.append(cards.pop(randint(0, len(cards) - 1)))
for i in range(numberOfPlayers):
    players.append(playerClass(input(f"Enter the name of player {i + 1}: "), initialChips))
    players[i].cards.append(cards.pop(randint(0, len(cards) - 1)))
    players[i].cards.append(cards.pop(randint(0, len(cards) - 1)))
    tempCards = players[i].cards + table.cards
    players[i].playableCards = playableCardsClass(tempCards.suits, tempCards.symbols)

#TODO: ADD ROUNDS, BETS, AND VISUALS

#TODO: MAYBE CHANGE THIS TO A FUNCTION IN THE hands CLASS
#CHECK POSSIBLE HANDS
for i in range(numberOfPlayers):
    if hands.royalFlush(players[i].playableCards.suits, players[i].playableCards.symbols):
        players[i].bestHand = 10  # Assign a high rank if a royal flush is detected

#TODO: REMOVE LATER
hands.flush([2, 3, 4, 5, 6, 7, 8])
for i in players:
    print(i)
for i in cards:
    print(i)