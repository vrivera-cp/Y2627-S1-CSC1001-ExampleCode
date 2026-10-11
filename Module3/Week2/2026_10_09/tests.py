import unittest
import function

class SongsByArtistsUnitTests(unittest.TestCase):
    def test_songs_by_artist_beatles(self) -> None:
        songs = ['Let It Be', 'Fur Elise', 'Hey Jude']
        artists = ['The Beatles', 'Mozart', 'The Beatles']
        artist = 'The Beatles'

        actual = function.songs_by_artist(songs, artists, artist)

        self.assertEqual(actual, ['Let It Be', 'Hey Jude'])

    def test_songs_by_artist_mozart(self) -> None:
        songs = ['Let It Be', 'Fur Elise', 'Hey Jude']
        artists = ['The Beatles', 'Mozart', 'The Beatles']
        artist = 'Mozart'

        actual = function.songs_by_artist(songs, artists, artist)

        self.assertEqual(actual, ['Fur Elise'])


    def test_songs_by_artist_not_in_artists(self) -> None:
        songs = ['Let It Be', 'Fur Elise', 'Hey Jude']
        artists = ['The Beatles', 'Mozart', 'The Beatles']
        artist = 'Weird Al'

        actual = function.songs_by_artist(songs, artists, artist)

        self.assertEqual(actual, [])

if __name__ == '__main__':
    unittest.main()