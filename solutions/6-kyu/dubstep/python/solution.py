def song_decoder(song):
    oldsong = song.replace("WUB", " ")
    return " ".join(oldsong.split())