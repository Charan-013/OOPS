class Song:
    def __init__(self,title,artist,album,genre,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def display_details(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, Genre: {self.genre}, Duration:{self.duration}s"
    
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    
    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,title):
        for ele in self.songs:
            if ele.title == title:
                self.songs.remove(ele)
                return True
        return False
    
    def get_songs(self):
        return self.songs
    
    def filter_songs(self,criteria,value):
        new = []
        if criteria == "genre":
            for ele in self.songs:
                if ele.genre == value:
                    new.append(ele)
        elif criteria == "artist":
            for ele in self.songs:
                if ele.artist == value:
                    new.append(ele)
        return new
    
    def search_songs(self,keyword):
        new = []
        for ele in self.songs:
            if ele.title == keyword or ele.title.lower() == keyword:
                new.append(ele)
            elif ele.artist == keyword or ele.title.lower() == keyword:
                new.append(ele)
            elif ele.album == keyword or ele.title.lower() == keyword:
                new.append(ele)
            elif ele.genre == keyword or ele.title.lower() == keyword:
                new.append(ele)
            
        return new
    
class PlaylistManager:
    def __init__(self):
        self.playlists = []


    def create_playlist(self,name):
        self.playlists.append(Playlist(name))
    

    def delete_playlist(self,name):
        for ele in self.playlists:
            if ele.name == name:
                self.playlists.remove(ele)
                return True
        return False
    

    def get_playlist(self,name):
        for ele in self.playlists:
            if ele.name == name:
                return ele
    
    def list_playlists(self):
        return self.playlists
    
    def cross_playlist_search(self,keyword):
        new = []
        for ele in self.playlists:
            new.extend(ele.search_songs(keyword))
        return new