n = int(input())
odd = set()
even = set()
current_line = 0
for _ in range (n):
    name = input()
    current_line += 1
    name_length = 0
    for char in name:
        name_length += ord(char)
    name_length = name_length // current_line
    if name_length % 2 == 0:
        even.add(name_length)
    else:
        odd.add(name_length)
if sum(odd) == sum(even):
    new_set = odd.union(even)
elif sum(odd) > sum(even):
    new_set = odd.difference(even)
else:
    new_set = odd.symmetric_difference(even)
print(', '.join([str(el) for el in new_set]))
