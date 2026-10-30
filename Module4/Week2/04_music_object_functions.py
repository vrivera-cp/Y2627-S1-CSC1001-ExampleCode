from classes import Song

def filter_by_artist(songs: list[Song], artist: str) -> list[Song]:
    """Return a list of songs with the given artist"""
    output = []

    for i in range(len(songs)):
        if artist in songs[i].artists: # True if the artists list contains the artist
            output.append(songs[i])

    return output

def name() -> None:
    """return a list of songs longer than the given duration"""

if __name__ == '__main__':
    songs = [
        Song('Let It Be', ['The Beatles'], 243),
        Song('Fur Elise', ['Mozart'], 60),
        Song('Hey Jude', ['The Beatles'], 23468),
        Song('Red Flags', ['Tom Cardy', 'Montaigne'], 23468),
        Song('Big Dumb Idiot', ['Tom Cardy'], 2345),
    ]

    artist = input("Search: ") # Must match casing exactly!
    print(filter_by_artist(songs, artist))