numbers = tuple([float(el) for el in input().split()])
occurrences = {}

for number in numbers:
    occurrences[number] = numbers.count(number)

for key, value in occurrences.items():
    print(f'{key:.1f} - {value} times')
