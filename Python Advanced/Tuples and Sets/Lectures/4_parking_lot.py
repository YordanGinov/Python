commands = int(input())
parked_cars = set()

for _ in range(commands):
    command, car_number = input().split(', ')
    if command == "IN":
        parked_cars.add(car_number)
    if command == "OUT":
        parked_cars.remove(car_number)

if len(parked_cars) <= 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(parked_cars))
