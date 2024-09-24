from collections import deque

quantity_of_food = int(input())
food_queue = deque()
queue = input().split()

for number in queue:
    food_queue.append(int(number))

print(max(food_queue))

while food_queue:
    food = int(food_queue.popleft())
    if quantity_of_food >= food:
        quantity_of_food -= food
    else:
        food_queue.appendleft(food)
        print(f'Orders left:', end= ' ')
        for number in food_queue:
            print(number, end= ' ')
        break
if len(food_queue) <= 0:
    print("Orders complete")