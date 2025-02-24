# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def matches(self, other):
        if self.rank == other.rank or self.suit == other.suit:
            return True
        return False

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck Class (without using random.shuffle)
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.manual_shuffle()

    def shuffle(self):
        pass

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def isEmpty(self):
        if len(self.cards) == 0:
            return True
        return False

    def manual_shuffle(self):
        """Manually shuffle the deck without using random"""
        shuffled = []
        while len(self.cards) > 0:
            mid = len(self.cards) // 2  # Pick a middle point
            shuffled.append(self.cards.pop(mid))  # Move card to shuffled deck
        self.cards = shuffled


# Hand Class
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def play_card(self, topCard):
        for card in self.cards:
            if card.matches(topCard):
                self.cards.remove(card)
                return card
        return None

    def hasCards(self):
        if len(self.cards) > 0:
            return True
        return False

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.isHuman = True

    def draw_card(self, deck):
        self.hand.add_card(deck.draw_card())

    def play_turn(self, topCard, deck):
        played_card = self.hand.play_card(topCard)
        if played_card:
            return played_card
        else:
            self.draw_card(deck)
            return None

    def hasWon(self):
        if len(self.hand.cards) == 0:
            return True
        return False

    def __str__(self):
        return f"{self.name}: {self.hand}"


# Game Class
class Game:
    def __init__(self, numPlayers):
        self.players = []
        self.deck = Deck()
        for i in range(numPlayers):
            self.players.append(Player(f"Player {i+1}"))
        self.topCard = self.deck.draw_card()
        # Deal 5 cards to each player
        for _ in range(5):
            for player in self.players:
                player.draw_card(self.deck)

    def startGame(self):
        print("Starting the game...")
        self.play_game()

    def play_game(self):
        current = 0
        while True:
            player = self.players[current]
            print(f"\n{player.name}'s Turn. Top Card: {self.topCard}")
            played = player.play_turn(self.topCard, self.deck)
            if played:
                self.topCard = played
                print(f"{player.name} played: {played}")
            else:
                print(f"{player.name} had to draw a card.")
            if player.hasWon():
                print(f"\n{player.name} wins the game!")
                break
            current = (current + 1) % len(self.players)

            if self.deck.isEmpty():
                print("\nDeck is empty. Game over.")
                break
