class Song:
    song_count = 0
    existing_artists = set()
    existing_genres = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
    
    @classmethod
    def add_song_to_count(cls):
        cls.song_count += 1
        return cls.song_count
    
    @classmethod
    def add_to_genres(cls):
        
    
    pass

Song1 = Song("Sunday Candy", "Chance the Rapper", "Rap")
print(Song.song_count)