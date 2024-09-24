from collections import deque

robots = input().split(';')
starting_time = input().split(':')
product = input()
products_queue = deque()
time_in_seconds = (int(starting_time[0]) * 3600) + (int(starting_time[1]) * 60) + int(starting_time[2])
robots_data = []
is_free = True
started_working = time_in_seconds
for robot in robots:
    name, work_time = robot.split('-')
    robots_data.append([name, work_time, is_free, started_working])

while product != "End":
    products_queue.append(product)
    product = input()

while products_queue and robots_data:
    counter = 0
    started_working += 1
    for current_robot in robots_data:
        if current_robot[3] + int(current_robot[1]) <= started_working:
            current_robot[2] = True
        if current_robot[2]:
            hours = started_working // 3600
            if hours >= 24:
                hours -= 24
                started_working = 0
            minutes = (started_working%3600)//60
            seconds = started_working%60
            print(f'{current_robot[0]} - {products_queue.popleft()} [{hours:02d}:{minutes:02d}:{seconds:02d}]')
            current_robot[2] = False
            current_robot[3] = started_working
            break
        counter += 1
    if counter >= len(robots_data):
        products_queue.rotate(-1)
