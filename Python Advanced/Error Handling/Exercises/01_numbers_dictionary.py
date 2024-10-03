data_map = {}
data = input()

while data != "Search":
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        data_map[data] = number
    data = input()

while data != "Remove":
    searched_number = input()
    try:
        print(data_map[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")
        if searched_number == "Remove":
            break
    data = input()

while data != "End":
    number_to_delete = input()
    try:
        del data_map[number_to_delete]
    except KeyError:
        print("Number does not exist in dictionary")
        if number_to_delete == "End":
            break
    data = input()

print(data_map)
