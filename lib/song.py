class Song:
    song_count = 0
    existing_artists = set()
    existing_genres = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.song_count += 1
        return cls.song_count
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.existing_genres.add(genre)
        return cls.existing_genres
    @classmethod
    def add_to_artists(cls, artist):
        cls.existing_artists.add(artist)
        return(cls.existing_artists)

Song1 = Song("Sunday Candy", "Chance the Rapper", "Rap")
Song2 = Song("Man I need", "Olivia Dean", "Pop")
Song3 = Song("Sunday In Brooklyn", "Kota the Friend", "Rap")
Song4 = Song("Colorado", "Kota the Friend", "Lofi")
print(Song.song_count)
print(Song.existing_genres)
print(Song.existing_artists)