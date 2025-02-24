class Person:
    def __init__(self,name,games):
        self.name = name
        self.games = games
    
    def add_game(self,game):
        if game not in self.games:
            self.games.append(game)

    def remove_game(self,game):
        self.games.remove(game)
    
    def get_favorite_games(self):
        return self.games
    
    def get_name(self):
        return self.name

    def __str__(self):
        # Person(name=John, games=['The Legend of Corgi', 'New Adventure'])
        return f"Person(name={self.name}, games={self.games})"
    
class SocialNetwork:
    def __init__(self):
        self.person = None
        self.users = []

    def add_user(self, user):
        for ele in self.users:
            if ele.name == user.name:
                print(f"User with name {user.name} already exists.")
                return

        self.users.append(user)


    def remove_user(self, user):
        for ele in self.users[:]:
            if ele.name == user:
                self.users.remove(ele)
                break
        else:
            print(f"User with name {user} not found.")


    def get_user(self,name):
        for ele in self.users:
            if ele.name == name:
                return ele
    
    def update_person(self, person):
        for ele in self.users:
            if ele.name == person.name:
                self.person = person
                break
        else:
            print(f"User {person.name} is not in the network.")

    
    def get_users_who_like(self,game):
        new = []
        for ele in self.users:
            for g in ele.games:
                if g == game:
                    new.append(ele.name)
        return new

    def __str__(self):
        # SocialNetwork(current person=None, users=[Person(name=John, games=['The Legend of Corgi', 'New Adventure']), Person(name=Alice, games=['Dinosaur Diner', 'The Movie: The Game']), Person(name=Bob, games=['The Legend of Corgi', 'Dinosaur Diner'])])
        s = ", ".join(str(ele) for ele in self.users)
        return f"SocialNetwork(current person=None, users=[{s}])"
