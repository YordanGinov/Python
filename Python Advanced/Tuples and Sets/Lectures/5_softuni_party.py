number_of_guests = int(input())
reservation_numbers = set()
for _ in range(number_of_guests):
    reservation_numbers.add(input())
guest = input()
while guest != "END" and reservation_numbers:
    if guest in reservation_numbers:
        reservation_numbers.remove(guest)
    guest = input()
print(f'{len(reservation_numbers)}')
for guest in sorted(reservation_numbers):
    print(guest)
