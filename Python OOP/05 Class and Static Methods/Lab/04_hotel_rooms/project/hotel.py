from project import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: Room(list) = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people):
        room = [el for el in self.rooms if el.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number: int):
        room = [el for el in self.rooms if el.number == room_number][0]
        room.free_room()

    def status(self):
        free_rooms = [str(el.number) for el in self.rooms if el.is_taken == False]
        taken_rooms = [str(el.number) for el in self.rooms if el.is_taken == True]
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}\n"
        return result