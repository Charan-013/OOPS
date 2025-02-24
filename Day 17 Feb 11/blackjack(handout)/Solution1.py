class Card:
    """
    Represents a single playing card with a numerical value.
    """
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def display_card(self):
        # Print the card’s value followed by a space.
        print(self.value, end=" ")


class Deck:
    """
    Manages a collection of Card objects in a fixed order.
    """
    def __init__(self):
        self.cards = []
        self.current_index = 0
        self.initialize_deck()

    def initialize_deck(self):
        # Clears any existing cards and repopulates the deck.
        self.cards.clear()
        # Fixed deck: the order is chosen so that:
        # Player's hand: 7, 1; Dealer's hand: 2, 3; then subsequent cards: 4, 5, 6.
        self.cards.append(Card(7))
        self.cards.append(Card(1))
        self.cards.append(Card(2))
        self.cards.append(Card(3))
        self.cards.append(Card(4))
        self.cards.append(Card(5))
        self.cards.append(Card(6))
        # You can add more cards if needed.

    def draw_card(self):
        # Returns the next card if available; otherwise, returns None.
        if self.current_index < len(self.cards):
            card = self.cards[self.current_index]
            self.current_index += 1
            return card
        else:
            return None

    def reset_deck(self):
        # Resets the index to start drawing from the beginning.
        self.current_index = 0


class Hand:
    """
    Represents a collection of cards held by a player or dealer.
    It maintains and calculates the total score with special Ace handling.
    """
    def __init__(self):
        self.cards_in_hand = []
        self.total_value = 0

    def add_card(self, card):
        self.cards_in_hand.append(card)
        self.calculate_score()

    def calculate_score(self):
        total = 0
        ace_count = 0
        # Count Aces as 11 initially.
        for card in self.cards_in_hand:
            val = card.get_value()
            if val == 1:
                ace_count += 1
                total += 11
            else:
                total += val

        # Adjust Aces from 11 to 1 if total > 21.
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        self.total_value = total

    def get_total_value(self):
        return self.total_value

    def display_hand(self):
        for card in self.cards_in_hand:
            card.display_card()
        print()  # New line

    def is_blackjack(self):
        # Blackjack if there are exactly 2 cards totaling 21.
        return len(self.cards_in_hand) == 2 and self.total_value == 21

    def has_busted(self):
        return self.total_value > 21


class Player:
    """
    Represents the human participant in the game.
    """
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.draw_card()
        if card is not None:
            self.hand.add_card(card)

    def stand(self):
        # No action required for stand.
        pass

    def get_score(self):
        return self.hand.get_total_value()

    def has_blackjack(self):
        return self.hand.is_blackjack()

    def has_busted(self):
        return self.hand.has_busted()

    def display_hand(self):
        self.hand.display_hand()


class Dealer:
    """
    Represents the dealer.
    """
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        card = deck.draw_card()
        if card is not None:
            self.hand.add_card(card)

    def play_turn(self, deck):
        print("Dealer's turn:")
        self.hand.display_hand()
        print("Dealer's total score:", self.hand.get_total_value())

        # Continue prompting while the dealer's score is below 17.
        # (Even though a real dealer would hit automatically, this simulation
        # allows input to simulate the dealer's decision.)
        while True:
            if self.hand.get_total_value() >= 17:
                break
            print("Dealer chooses to hit. (h/s): ",end=" ")
            decision = input().strip().lower()
            if decision == 'h':
                self.hit(deck)
                self.hand.display_hand()
                print("Dealer's total score:", self.hand.get_total_value())
                if self.hand.has_busted():
                    break
            elif decision == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")
        # print("Dealer's final hand:")
        self.hand.display_hand()
        print("Dealer's total score:", self.hand.get_total_value())

    def get_score(self):
        return self.hand.get_total_value()

    def display_hand(self):
        self.hand.display_hand()

    def has_busted(self):
        return self.hand.has_busted()


class Game:
    """
    Controls the overall game flow, managing interactions among Deck, Player, and Dealer.
    """
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        print("Game starts:")
        self.deck.reset_deck()
        # Deal two cards to the player and two to the dealer.
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)

    def player_turn(self):
        while True:
            print("Player's turn:")
            self.player.display_hand()
            print("Your total score:", self.player.get_score())
            if self.player.has_busted():
                print("Player busts!")
                break
            print("Dealer chooses to hit. (h/s): ",end=" ")
            decision = input().strip().lower()
            # decision = input("Do you want to hit or stand? (h/s): ").strip().lower()
            if decision == 'h':
                self.player.hit(self.deck)
                if self.player.has_busted():
                    print("Player busts!")
                    break
            elif decision == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def dealer_turn(self):
        if not self.player.has_busted():
            self.dealer.play_turn(self.deck)

    def determine_winner(self):
        print("\nFinal results:")
        self.player.display_hand()
        self.dealer.display_hand()
        if self.player.has_busted():
            print("Player has busted!")
        elif self.dealer.has_busted():
            print("Dealer has busted! Player wins!")
        else:
            player_score = self.player.get_score()
            dealer_score = self.dealer.get_score()
            if player_score > dealer_score:
                print("Player wins!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")

    def play_game(self):
        self.start_game()
        self.player_turn()
        self.dealer_turn()
        self.determine_winner()


if __name__ == "__main__":
    # Create and run the game.
    game = Game()
    game.play_game()
