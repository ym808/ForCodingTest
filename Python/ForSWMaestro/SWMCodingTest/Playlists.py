playlists = [["a","b"],["b","a","c","b"]]
play_count = {}
song_seen = {}

cur_play = 0

for playlist in playlists:
    for song in playlist:
        play_count[song] = play_count.get(song, 0) + 1
        song_seen[song] = song_seen.get(song, cur_play)

        cur_play += 1
songs = list(play_count.keys())
songs.sort(key=lambda x: (-play_count[x], song_seen[x]))
print(" ".join(songs))