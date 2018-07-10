songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

# Set Comprehension: Correct Solution

good_songs = {(song[0], song[1]) for song in songs if song[0] != 'Nickelback'}

print(good_songs)

print(type(good_songs))

# Dictionary Comprehension: Outside scope of this lesson (Solution 1)

# dictionary_songs = dict(songs)
# no_nickel = {}

# for artist, song in dictionary_songs.items():
#     no_nickel_local = {}
#     if artist != 'Nickelback':
#         no_nickel_local.update({artist: song})
#     no_nickel.update(no_nickel_local)

# print(no_nickel)





