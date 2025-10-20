from project import Song
class Album:
    def __init__(self, name: str, *args: tuple[Song]) -> None:
        self.name = name
        self.songs: list[Song] = [el for el in args]
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        elif song not in self.songs and self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            current_song = [el for el in self.songs if el.name == song_name][0]
            if self.published:
                return f"Cannot remove songs. Album is published."
            self.songs.remove(current_song)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result