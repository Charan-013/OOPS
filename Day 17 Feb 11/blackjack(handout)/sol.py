import random

class Card:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def displayCard(self):
        print(self.value, end=" ")

class Deck:
    def __init__(self):
        self.cards = []
        self.currentIndex = 0
        self.initializeDeck()

    def initializeDeck(self):
        """Populates a deck with predefined cards in order for a fixed sequence."""
        self.cards.clear()
        self.cards = [
            Card(7), Card(1), Card(2), Card(3), Card(4), Card(5), Card(6)
        ]
        self.currentIndex = 0

    def drawCard(self):
        """Returns the next available card from the deck."""
        if self.currentIndex < len(self.cards):
            card = self.cards[self.currentIndex]
            self.currentIndex += 1
            return card
        return None  # No more cards available

    def resetDeck(self):
        """Resets the deck to the beginning."""
        self.currentIndex = 0

class Hand:
    def __init__(self):
        self.cardsInHand = []
        self.totalValue = 0

    def addCard(self, card):
        """Adds a card to the hand and updates the score."""
        self.cardsInHand.append(card)
        self.calculateScore()

    def calculateScore(self):
        """Calculates the total value of the hand, handling Ace as 1 or 11 optimally."""
        self.totalValue = sum(card.getValue() for card in self.cardsInHand)
        ace_count = sum(1 for card in self.cardsInHand if card.getValue() == 1)

        while self.totalValue <= 11 and ace_count > 0:
            self.totalValue += 10  # Treat Ace as 11
            ace_count -= 1

    def getTotalValue(self):
        """Returns the current hand value."""
        return self.totalValue

    def displayHand(self):
        """Displays the player's hand."""
        for card in self.cardsInHand:
            card.displayCard()
        print()

    def isBlackjack(self):
        """Returns True if the hand is a blackjack (exactly two cards summing 21)."""
        return len(self.cardsInHand) == 2 and self.totalValue == 21

    def hasBusted(self):
        """Returns True if the player has exceeded 21."""
        return self.totalValue > 21

class Player:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        """Player takes a card from the deck."""
        card = deck.drawCard()
        if card:
            self.hand.addCard(card)

    def stand(self):
        """Player chooses to stand."""
        pass

    def getScore(self):
        """Returns player's score."""
        return self.hand.getTotalValue()

    def hasBlackjack(self):
        """Returns True if the player has a blackjack."""
        return self.hand.isBlackjack()

    def hasBusted(self):
        """Returns True if the player has busted."""
        return self.hand.hasBusted()

    def displayHand(self):
        """Displays the player's hand."""
        self.hand.displayHand()

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        """Dealer takes a card from the deck."""
        card = deck.drawCard()
        if card:
            self.hand.addCard(card)

    def playTurn(self, deck):
        """Dealer's turn: must hit until 17 or more is reached."""
        while self.getScore() < 17:
            print("Dealer chooses to hit.")
            card = deck.drawCard()
            if card is None:
                print("No more cards in deck. Dealer stands.")
                break
            self.hand.addCard(card)
            self.displayHand()

    def getScore(self):
        """Returns dealer's score."""
        return self.hand.getTotalValue()

    def displayHand(self):
        """Displays the dealer's hand."""
        self.hand.displayHand()
        
    def hasBlackjack(self):
        """Returns True if the dealer has a blackjack."""
        return self.hand.isBlackjack()

    def hasBusted(self):
        """Returns True if the dealer has busted."""
        return self.hand.hasBusted()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def startGame(self):
        """Starts the game by resetting deck and dealing initial hands."""
        print("Game starts:")
        self.deck.resetDeck()

        # Deal two cards to player and dealer
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)

    def playerTurn(self):
        """Handles the player's turn."""
        while True:
            print("Player's turn:")
            self.player.displayHand()
            print(f"Your total score: {self.player.getScore()}")
            if self.player.hasBlackjack():
                print("Blackjack! You might win instantly.")
                return
            elif self.player.hasBusted():
                print("You busted!")
                return

            choice = input("Do you want to hit or stand? (h/s): ").strip().lower()
            if choice == 'h':
                self.player.hit(self.deck)
            elif choice == 's':
                break

    def dealerTurn(self):
        """Handles the dealer's turn if the player has not busted."""
        if not self.player.hasBusted():
            print("Dealer's turn:")
            self.dealer.displayHand()
            print(f"Dealer's total score: {self.dealer.getScore()}")
            self.dealer.playTurn(self.deck)
            print("Dealer's final hand:")
            self.dealer.displayHand()
            print(f"Dealer's total score: {self.dealer.getScore()}")

    def determineWinner(self):
        """Determines and prints the game result."""
        player_score = self.player.getScore()
        dealer_score = self.dealer.getScore()

        print("\nFinal results:")
        self.player.displayHand()
        self.dealer.displayHand()

        if self.player.hasBusted():
            print("Dealer wins!")
        elif self.dealer.hasBusted():
            print("Player wins!")
        elif self.player.hasBlackjack() and not self.dealer.hasBlackjack():
            print("Player wins with a Blackjack!")
        elif self.dealer.hasBlackjack() and not self.player.hasBlackjack():
            print("Dealer wins with a Blackjack!")
        elif player_score > dealer_score:
            print("Player wins!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def playGame(self):
        """Runs the full game flow."""
        self.startGame()
        self.playerTurn()
        self.dealerTurn()
        self.determineWinner()

def main():
    game = Game()
    game.playGame()

if __name__ == "__main__":
    main()
