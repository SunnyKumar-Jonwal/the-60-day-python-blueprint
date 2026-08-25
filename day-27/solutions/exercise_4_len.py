class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


playlist = Playlist(["Song A", "Song B", "Song C"])
print(len(playlist))
