class Song:
    count = 0
    artists = set()
    genres = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)
        cls.add_to_genre_count(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)
        cls.add_to_artists_count(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1
    
    @classmethod
    def add_to_artists_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

Song1 = Song("Sunday Candy", "Chance the Rapper", "Rap")
Song2 = Song("Man I need", "Olivia Dean", "Pop")
Song3 = Song("Sunday In Brooklyn", "Kota the Friend", "Rap")
Song4 = Song("Colorado", "Kota the Friend", "Lofi")

print(Song.count)