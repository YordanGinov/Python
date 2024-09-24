from collections import deque
single_line = deque(input().split())
main_color = ["red", "yellow", "blue", "orange", "purple", "green"]
colors_created = []

while single_line:
    first_string = single_line.popleft()
    second_string = single_line.pop() if single_line else ''
    if first_string+second_string in main_color:
        colors_created.append(first_string+second_string)
    elif  second_string+first_string in main_color:
        colors_created.append(second_string+first_string)
    else:
        if len(first_string) > 1:
            single_line.insert(len(single_line)//2, first_string[:-1])
        if len(second_string) > 1:
            single_line.insert(len(single_line)//2, second_string[:-1])
for color in colors_created:
    if color == "orange":
        if "red" not in colors_created or "yellow" not in colors_created:
            colors_created.remove(color)
    elif color == "purple":
        if "red" not in colors_created or "blue" not in colors_created:
            colors_created.remove(color)
    elif color == "green":
        if "yellow" not in colors_created or "blue" not in colors_created:
            colors_created.remove(color)
print(colors_created)
