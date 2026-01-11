class Song:
    song_count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        print(self.name, self.artist, self.genre)
    
    pass

Song1 = Song("Sunday Candy", "Chance the Rapper", "Soulful Rap")
