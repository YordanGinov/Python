from collections import deque

kids = deque(input().split())
turns = int(input())

while len(kids) > 1:
    for i in range(turns-1):
        kid = kids.popleft()
        kids.append(kid)
    print(f"Removed {kids.popleft()}")
print(f"Last is {kids.popleft()}")


# names = deque([])
# program_input = input().split()
# tosses = int(input())
# current_toss = tosses - 1
#
# for name in program_input:
#     names.append(name)
#
# while len(names) > 1:
#     if current_toss != 0:
#         current_toss -= 1
#         names.rotate(-1)
#     else:
#         current_toss = tosses - 1
#         print(f'Removed {names.popleft()}')
# print(f'Last is {names.popleft()}')
