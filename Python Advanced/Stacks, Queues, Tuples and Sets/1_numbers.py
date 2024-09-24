first_set = set(input().split())
second_set = set(input().split())
n = int(input())
is_subset = False

for _ in range(n):
    command = input().split()
    #cmd = f'{command[0]} {command[1]}'
    #numbers = [number for number in user_input[2:]
    if command[0] == "Add" and command[1] == "First":
        for index in range(2, len(command)):
            first_set.add(command[index])
    elif command[0] == "Add" and command[1] == "Second":
        for index in range(2, len(command)):
            second_set.add(command[index])
    elif command[0] == "Remove" and command[1] == "First":
        for index in range(2, len(command)):
            if command[index] in first_set:
                first_set.remove(command[index])
    elif command[0] == "Remove" and command[1] == "Second":
        for index in range(2, len(command)):
            if command[index] in second_set:
                second_set.remove(command[index])
    else:
        if first_set.issubset(second_set):
            is_subset = True
        elif second_set.issubset(first_set):
            is_subset = True
        print(is_subset)

sorted_first_set = sorted([int(el) for el in first_set])
sorted_second_set = sorted([int(el) for el in second_set])
print(', '.join([str(el) for el in sorted_first_set]))
print(', '.join([str(el) for el in sorted_second_set]))
#print(*sorted(first_set), sep=', '
