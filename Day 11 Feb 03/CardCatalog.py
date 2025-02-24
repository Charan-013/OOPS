class CardClass:
    def __init__(self, title, author, subject):
        self.bookTitle = title
        self.bookAuthor = author
        self.bookSubject = subject


class CardCatlog:
    def __init__(self):
        self.cards = []

    def addACard(self, title, author, subject):
        # self.cards.append(CardClass(title,author,subject))
        card = CardClass(title, author, subject)
        self.cards.append(card)

    def getATitle(self, title):
        for ele in self.cards:
            if ele.bookTitle == title:
                return ele.bookTitle, ele.bookAuthor, ele.bookSubject

    def getAnAuthor(self, author):
        bookByAuthor = []
        for ele in self.cards:
            if ele.bookAuthor == author:
                bookByAuthor.append(ele.bookTitle)
        return bookByAuthor

    def getSubject(self, subject):
        booksBySubject = []
        for ele in self.cards:
            if ele.bookSubject == subject:
                booksBySubject.append(ele.bookTitle)
        return booksBySubject

    def removeATitle(self, title):
        new_cards = []
        for ele in self.cards:
            if ele.bookTitle != title:
                new_cards.append(ele)
        self.cards = new_cards
        self.cards = [ele for ele in self.cards if ele.bookTitle != title]
        # print(self.cards)

    def printTheCatalog(self):
        for ele in self.cards:
            print(f"{ele.bookTitle} {ele.bookAuthor} {ele.bookSubject}")


def cardCatalog():
    cc = CardCatlog()
    while True:
        try:
            inp = input().strip()

            if not inp:
                break

            if inp.startswith("add"):
                inp = inp.split("add ")
                inp = inp[1].split(",")
                title = inp[0]
                author = inp[1]
                subject = inp[2]
                cc.addACard(inp[0], inp[1], inp[2])
                print(f"Card add successfully : {title} {author} {subject}")

            elif inp.startswith("getTitle"):
                inp = inp.split("getTitle ")
                inp = inp[1]
                print(cc.getATitle(inp))

            elif inp.startswith("getAuthor"):
                inp = inp.split("getAuthor ")
                inp = inp[1]
                print(f"Book by Author :  {cc.getAnAuthor(inp)}")

            elif inp.startswith("getSubject"):
                inp = inp.split("getSubject ")
                inp = inp[1]
                print(f"Book by Subjects :  {cc.getSubject(inp)}")

            elif inp.startswith("printCatlog"):
                cc.printTheCatalog()

            elif inp.startswith("remove"):
                inp = inp.split("remove ")
                inp = inp[1]  
                cc.removeATitle(inp)  
                print(f"Removed Book with title: {inp}")

        except EOFError:
            break


if __name__ == "__main__":
    cardCatalog()

