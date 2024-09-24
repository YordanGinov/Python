from collections import deque

dispenser_liters = int(input())
water_line = deque([])

name = input()
while name != "Start":
    water_line.append(name)
    name = input()

query = input()
while query != "End":
    query = query.split()
    if query[0] == "refill":
        dispenser_liters += int(query[1])
    else:
        if dispenser_liters >= int(query[0]):
            print(f'{water_line.popleft()} got water')
            dispenser_liters -= int(query[0])
        else:
            print(f'{water_line.popleft()} must wait')
    query = input()
print(f'{dispenser_liters} liters left')