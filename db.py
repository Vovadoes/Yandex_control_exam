import sqlite3


class Track:
    def __init__(self, name):
        self.name = name
        connection = sqlite3.connect(name)
        self.cursor = connection.cursor()

    def print_albums(self, genre):
        result = self.cursor.execute('''SELECT DISTINCT Album.Title 
                                        FROM Album
                                        JOIN Track ON Album.AlbumId = Track.AlbumId
                                        JOIN Genre ON Genre.GenreId = Track.GenreId
                                        WHERE Genre.Name = ?
                                        ORDER BY Album.Title''', (genre, )).fetchall()
        for line in result:
            print(line[0])

    def print_tracks(self, genre):
        result = self.cursor.execute('''SELECT Artist.Name, Genre.Name, Track.Name
                                        FROM Artist
                                        JOIN Album ON Album.ArtistId = Artist.ArtistId
                                        JOIN Track ON Album.AlbumId = Track.AlbumId
                                        JOIN Genre ON Genre.GenreId = Track.GenreId
                                        WHERE Genre.Name = ?
                                        ORDER BY Milliseconds''', (genre,)).fetchall()
        return result

bd = Track('Chinook_Sqlite.sqlite')
bd.print_albums('Rock')
print(*bd.print_tracks('Rock'))