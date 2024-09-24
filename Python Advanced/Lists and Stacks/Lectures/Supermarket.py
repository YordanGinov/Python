from collections import deque

query = input()
queue = deque([])

while query != "End":
    if query == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(query)
    query = input()
print(f'{len(queue)} people remaining.')
