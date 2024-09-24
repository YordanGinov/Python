from collections import deque

green_light_duration= int(input())
free_window_duration= int(input())
current_green_light_duration = green_light_duration
current_free_window_duration = free_window_duration
cars_in_line = deque()
total_cars_passed = 0
current_car= ''
checked_car = ''
hit_symbol = ''
is_crash = False

query = input()
while query != "END" and not is_crash:
    if query == "green":
        current_green_light_duration = green_light_duration
        current_free_window_duration = free_window_duration
        while (current_green_light_duration > 0 or current_free_window_duration > 0) and cars_in_line:
            if current_green_light_duration > 0:
                current_car = cars_in_line.popleft()
                checked_car = current_car
            elif len(current_car) <= 0:
                break
            for char in range(len(current_car)):
                if current_green_light_duration > 0:
                    current_green_light_duration -= 1
                elif current_free_window_duration > 0:
                    current_free_window_duration -= 1
                if current_green_light_duration == 0 and current_free_window_duration == 0 and len(current_car) > char + 1:
                    is_crash = True
                    hit_symbol = current_car[char + 1]
                    break
                elif len(current_car) <= char + 1:
                    total_cars_passed += 1
                    current_car = ''
    else:
        cars_in_line.append(query)
    query = input()

if is_crash:
    print(f'A crash happened!')
    print(f'{checked_car} was hit at {hit_symbol}.')
else:
    print("Everyone is safe.")
    print(f'{total_cars_passed} total cars passed the crossroads.')
