from classes import Song

def playlist_duration(songs: list[Song]) -> int:
    # 1. Initialize Accumulator
    total_duration = 0

    # 2. Iterate over items
    for song in songs:
        # 3. Combine each element into the accumulator
        total_duration += song.duration # note the attribute access

    # 4. Return the accumulator
    return total_duration

if __name__ == '__main__':
    # Billboard Hot 100, Week of Oct 31, 2026
    songs = [
        Song('Choosin\' Texas', ['Ella Langley'], 192),
        Song('Housewife', ['Tate McRae'], 208),
        Song('Expectations', ['Olivia Rodrigo', 'Chappell Roan'], 223),
        Song('Lies', ['Zach Brya', 'Lana Del Rey'], 220),
        Song('Patient Zero', ['Taylor Swift'], 225),
        Song('Boston', ['Stella Lefty'], 170),
        Song('Been By Now', ['Morgan Wallen'], 213),
        Song('Dracula', ['Tame Impala', 'JENNIE'], 205),
        Song('Nicole Kidman', ['ADELA'], 181),
        Song('Stupid Song', ['Olivia Rodrigo'], 209),
    ]

    total_duration = playlist_duration(songs)

    # Conversions to display the time how a real-world program might
    minutes = total_duration // 60
    seconds = total_duration % 60

    print(f'Playlist Duration: {minutes}:{seconds:02}')