import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def matches(self, other):
        if self.rank == other.rank or self.suit == other.suit:
            return True
        return False
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.manual_shuffle()
        
    def shuffle(self):
        pass

    def manual_shuffle(self):
        shuffled = []
        while self.cards:
            mid = len(self.cards) // 2
            shuffled.append(self.cards.pop(mid))
        self.cards = shuffled

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def play_card(self, top_card):
        for ele in self.cards:
            if ele.matches(top_card):
                self.cards.remove(ele)
                return ele
        return None

    def has_cards(self):
        return len(self.cards) > 0

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.hand = Hand()
        self.is_human = is_human

    def draw_card(self, deck):
        if not deck.is_empty():
            self.hand.add_card(deck.draw_card())

    def play_turn(self, top_card, deck):
        played_card = self.hand.play_card(top_card)
        if played_card:
            return played_card
        self.draw_card(deck)
        return None

    def has_won(self):
        return not self.hand.has_cards()

    def __str__(self):
        return f"{self.name}: {self.hand}"


class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.top_card = self.deck.draw_card()
        self.current_player_index = 0

        for player in self.players:
            for _ in range(5):
                player.draw_card(self.deck)

    def start_game(self):
        # print("Game started! Top card is:", self.top_card)
        self.play_game()

    def play_game(self):
        while True:
            player = self.players[self.current_player_index]
            print(f"\n{player.name}'s Turn. Top Card: {self.top_card}")
            played_card = player.play_turn(self.top_card, self.deck)
            
            if played_card:
                print(f"{player.name} played: {played_card}")
                self.top_card = played_card
                if player.has_won():
                    print()
                    print(f"{player.name} wins the game!")
                    break
            else:
                print(f"{player.name} had to draw a card.")

            self.current_player_index = (self.current_player_index + 1) % len(self.players)


