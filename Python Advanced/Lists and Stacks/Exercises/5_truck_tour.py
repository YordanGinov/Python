from collections import deque

petrol_pumps = int(input())
petrol_pump_data = deque()

for _ in range(petrol_pumps):
    current_fuel, distance = input().split()
    petrol_pump_data.append([int(current_fuel), int(distance)])

starting_position = 0
pump_stops = 0

while pump_stops < petrol_pumps:
    fuel = 0
    for index in range(petrol_pumps):
        fuel += petrol_pump_data[index][0]
        destination = petrol_pump_data[index][1]
        if fuel < destination:
            petrol_pump_data.rotate(-1)
            starting_position += 1
            pump_stops = 0
            break
        fuel -= destination
        pump_stops += 1
print(starting_position)
