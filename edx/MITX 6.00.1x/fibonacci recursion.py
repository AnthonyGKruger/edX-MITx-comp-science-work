
song_decoder = lambda song :' '.join([x for x in song.split('WUB') if x != ''])


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))


