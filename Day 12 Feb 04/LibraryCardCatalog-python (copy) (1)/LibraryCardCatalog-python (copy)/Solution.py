class Card:
    def __init__(self, title, author, subject):
        self.bookTitle = title
        self.bookAuthor = author
        self.bookSubject = subject



class CardCatalog:
    def __init__(self):
        self.cards = []

    def add_a_card(self, card):
        self.cards.append(card)
        self.cards.sort(key=lambda x: (x.bookTitle.lower(), not x.bookTitle.islower()))
        # self.cards.append(card)
        # self.cards.sort(key=lambda x:x.bookTitle)

    def get_a_title(self, title):
        for ele in self.cards[::-1]:
            if ele.bookTitle == title:
                return f"Title: {ele.bookTitle} | Author: {ele.bookAuthor} | Subject: {ele.bookSubject}"
            elif ele.bookTitle.lower() == title:
                return f"Title: {ele.bookTitle} | Author: {ele.bookAuthor} | Subject: {ele.bookSubject}"
        
    
    def get_an_author(self, author):
        bookByAuthor = []
        for ele in self.cards:
            if ele.bookAuthor == author or ele.bookAuthor.lower() == author:
                bookByAuthor.append(f"Title: {ele.bookTitle} | Author: {ele.bookAuthor} | Subject: {ele.bookSubject}")
        return bookByAuthor
    
    def get_subject(self, subject):
        booksBySubject = []
        for ele in self.cards:
            if ele.bookSubject == subject or ele.bookSubject.lower() == subject:
                booksBySubject.append(f"Title: {ele.bookTitle} | Author: {ele.bookAuthor} | Subject: {ele.bookSubject}")
        return booksBySubject

    def remove_a_title(self, title):
        for i in range(len(self.cards) - 1, -1, -1):
            card = self.cards[i]
            if card.bookTitle == title or card.bookTitle.lower() == title:
                del self.cards[i]
                return True
        return False

    def print_the_catalog(self):
        if self.cards == []:
            print(f"The catalog is empty.")
        for ele in self.cards:
            print(f"Title: {ele.bookTitle} | Author: {ele.bookAuthor} | Subject: {ele.bookSubject}")

