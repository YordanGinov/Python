n, m = [int(x) for x in input().split(", ")]
matrix = []
mission_timer = 16
ct_position = []
bomb_position = []
has_exploded = False
ct_alive = True
bomb_defused = False
mapper ={
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def end_of_game(exploded, ct_alive, bomb_defused):
    if not ct_alive:
        return True
    if bomb_defused:
        return True
    if exploded:
        return True
    return False

def next_position(current_command, mapper, ct_position):
    current_row_index, current_col_index = ct_position
    future_ct_position_row = current_row_index + mapper[current_command][0]
    future_ct_position_column = current_col_index + mapper[current_command][1]
    return future_ct_position_row, future_ct_position_column

for i in range(n):
    current_input = input()
    matrix.append([])
    for j in range(m):
        matrix[i].append(current_input[j])
        if current_input[j] == "C":
            ct_position = [i, j]
        elif current_input[j] == "B":
            bomb_position = [i, j]

while True:
    command = input()
    if mission_timer < 0 and ct_position != bomb_position:
        break
    if command == "defuse":
        if matrix[ct_position[0]][ct_position[1]] == "B":
            mission_timer -= 4
            if mission_timer < 0:
                has_exploded = True
            elif mission_timer >= 0:
                bomb_defused = True
                matrix[ct_position[0]][ct_position[1]] = "D"
                has_exploded = False
            break
        else:
            mission_timer -= 2
            if mission_timer < 0:
                has_exploded = True
                break
            continue
    if end_of_game(has_exploded ,ct_alive, bomb_defused):
        break
    if mission_timer > 0:
        mission_timer -= 1
    elif mission_timer == 0:
        has_exploded = True
        break
    future_ct_position = next_position(command, mapper, ct_position)
    if future_ct_position[0] >= n or future_ct_position[1] >= m or future_ct_position[0] < 0 or future_ct_position[1] < 0:
        continue
    elif matrix[future_ct_position[0]][future_ct_position[1]] == "*" or matrix[future_ct_position[0]][future_ct_position[1]] == "B":
        ct_position = future_ct_position
    elif matrix[future_ct_position[0]][future_ct_position[1]] == "T":
        ct_alive = False
        matrix[future_ct_position[0]][future_ct_position[1]] = "*"
        break
if mission_timer < 0 :
    has_exploded = True
if has_exploded and ct_alive:
    print("Terrorists win!")
    if matrix[ct_position[0]][ct_position[1]] == matrix[bomb_position[0]][bomb_position[1]]:
        matrix[ct_position[0]][ct_position[1]] = "X"
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(mission_timer)} second/s.")
    else:
        print("Bomb was not defused successfully!")
        print(f"Time needed: 0 second/s.")

elif ct_alive and bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {mission_timer} second/s remaining.")
elif not ct_alive:
    print("Terrorists win!")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="")
    print()