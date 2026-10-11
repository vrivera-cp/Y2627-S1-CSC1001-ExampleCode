
songs = ['Let It Be', 'Fur Elise', 'Hey Jude']
artists = ['The Beatles', 'Mozart', 'The Beatles']

# Example 1: With above data, searching for 'The Beatles' yields: ['Let it Be', 'Hey Jude']

def songs_by_artist(songs :list[str], artists :list[str], artist: str) -> list[str]:

    artist_indexes = []
    for i in range(len(artists)):
        index = i
        artist_indexes.append(index)

    filtered_indexes = []
    for index in artist_indexes:
        if artists[index] == artist:
            filtered_indexes.append(index)

    filtered_songs = []
    for filtered_index in filtered_indexes:
        filtered_song = songs[filtered_index]
        filtered_songs.append(filtered_song)

    return filtered_songs

def songs_by_artist_one_line(songs :list[str], artists :list[str], artist: str) -> list[str]:
    return [songs[i] for i in range(len(songs)) if artists[i] == artist]

if __name__ == '__main__':
    filtered_songs = songs_by_artist_one_line(songs, artists, 'The Beatles')
    print(filtered_songs)