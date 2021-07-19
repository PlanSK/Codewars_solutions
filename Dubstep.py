def song_decoder(song):
    return ' '.join([value for value in song.split('WUB') if value])


a = 'AWUBBWUBC'
b = 'AWUBWUBWUBBWUBWUBWUBC'
c = 'WUBAWUBBWUBCWUB'
print(song_decoder(a))
print(song_decoder(b))
print(song_decoder(c))