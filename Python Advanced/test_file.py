def accommodate(*guests, **room_data):
    full_rooms = {}
    not_accomodated = 0
    accomodations = 0
    for guest in guests:
        for room in room_data:
            if guest <= room_data[room]:
                accomodations += 1
                current_room = room.split('_')
                full_rooms[current_room[1]] = guest
                room_data.pop(room)
                break
            else:
                not_accomodated += guest
    if not_accomodated > 0:
        print(f"Guests with no accommodation: {not_accomodated}")
    if accomodations > 0:
        print(f"A total of {accomodations} accommodations were completed!")
        for room in full_rooms:
            print(f"<Room {room} accomodates {full_rooms[room]} guests>")




print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))