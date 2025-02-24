class Card:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def displayCard(self):
        # Display the card’s value followed by a space
        print(self.value, end=" ")


class Deck:
    def __init__(self):
        self.cards = []
        self.currentIndex = 0

    def initializeDeck(self):
        self.cards.clear()
        # Fixed set: first card is 7, followed by cards 1 to 6.
        self.cards.append(Card(7))
        for i in range(1, 7):
            self.cards.append(Card(i))
        self.resetDeck()

    def drawCard(self):
        if self.currentIndex < len(self.cards):
            card = self.cards[self.currentIndex]
            self.currentIndex += 1
            return card
        return None

    def resetDeck(self):
        self.currentIndex = 0


class Hand:
    def __init__(self, cardsInHand=None, totalValue=0):
        if cardsInHand is None:
            cardsInHand = []
        self.cardsInHand = cardsInHand
        self.totalValue = totalValue

    def addCard(self, card):
        self.cardsInHand.append(card)
        self.calculateScore()

    def calculateScore(self):
        self.totalValue = 0
        ace_count = 0
        for card in self.cardsInHand:
            # Treat Ace (value 1) as 11 initially.
            if card.getValue() == 1:
                ace_count += 1
                self.totalValue += 11
            else:
                self.totalValue += card.getValue()
        # Adjust Aces from 11 to 1 as needed.
        while self.totalValue > 21 and ace_count > 0:
            self.totalValue -= 10
            ace_count -= 1

    def getTotalValue(self):
        return self.totalValue

    def displayHand(self):
        for card in self.cardsInHand:
            card.displayCard()
        print()  # Newline after displaying cards

    def isBlackjack(self):
        return len(self.cardsInHand) == 2 and self.totalValue == 21

    def hasBusted(self):
        return self.totalValue > 21


class Player:
    def __init__(self, hand):
        self.hand = hand
        self.stood = False  # Indicates whether the player has chosen to stand

    def hit(self, deck):
        card = deck.drawCard()
        if card is not None:
            self.hand.addCard(card)

    def stand(self):
        self.stood = True

    def getScore(self):
        return self.hand.getTotalValue()

    def hasBlackjack(self):
        return self.hand.isBlackjack()

    def hasBusted(self):
        return self.hand.hasBusted()

    def displayHand(self):
        self.hand.displayHand()

    def isStanding(self):
        return self.stood


class Dealer:
    def __init__(self, hand):
        self.hand = hand

    def hit(self, deck):
        card = deck.drawCard()
        if card is not None:
            self.hand.addCard(card)

    def playTurn(self, scanner, deck):
        # Dealer automatically hits until reaching a score of 17 or higher.
        while self.getScore() < 17 and not self.hasBusted():
            print("Dealer chooses to hit.")
            self.hit(deck)
            print("Dealer's hand: ", end="")
            self.displayHand()
            print(f"Dealer's total score: {self.getScore()}")
        if self.getScore() >= 17 and not self.hasBusted():
            print("Dealer stands.")

    def getScore(self):
        return self.hand.getTotalValue()

    def displayHand(self):
        self.hand.displayHand()

    def hasBusted(self):
        return self.hand.hasBusted()


class Game:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def startGame(self):
        self.deck.initializeDeck()
        print("Game starts:")
        print("Player's turn:")
        # Deal two cards each.
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.displayHand()
        print(f"Your total score: {self.player.getScore()}")

    def playerTurn(self, scanner):
        # Continue until the player stands or busts.
        while not self.player.isStanding() and not self.player.hasBusted():
            choice = scanner("Do you want to hit or stand? (h/s): ").strip().lower()
            if choice == 'h':
                self.player.hit(self.deck)
                # The hand automatically recalculates its score when a card is added.
                if self.player.hasBusted():
                    break
                print("Player's turn:")
                self.player.displayHand()
                print(f"Your total score: {self.player.getScore()}")
            elif choice == 's':
                self.player.stand()
                print("Player stands.")
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    def dealerTurn(self, scanner):
        if not self.player.hasBusted():
            print("Dealer's turn:")
            self.dealer.playTurn(scanner, self.deck)

    def determineWinner(self):
        print("\nFinal results:")
        print("Player's hand: ", end="")
        self.player.displayHand()
        print(f"Player's total score: {self.player.getScore()}")
        print("Dealer's hand: ", end="")
        self.dealer.displayHand()
        print(f"Dealer's total score: {self.dealer.getScore()}")

        if self.player.hasBusted():
            print("Player has busted!")
        elif self.dealer.hasBusted():
            print("Dealer has busted!")
        elif self.player.getScore() > self.dealer.getScore():
            print("Player wins!")
        elif self.player.getScore() < self.dealer.getScore():
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def playGame(self, scanner):
        self.startGame()
        self.playerTurn(scanner)
        self.dealerTurn(scanner)
        self.determineWinner()


def main():
    deck = Deck()
    player = Player(Hand())
    dealer = Dealer(Hand())
    game = Game(deck, player, dealer)
    game.playGame(input)


if __name__ == "__main__":
    main()
