playlist = {
    "title": "my_songs",
    "author": "Rox",
    "songs" : [
    {"title": "song1", "artist": ["Lucretia"], "duration": 3.5},
    {"title": "song2", "artist": ["Ian", "DjMelanie"],"duration": 4.2},
    {"title": "song3", "artist": ["Nasi"], "duration": 4.2}
    ]
}

total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]

print(total_length)
