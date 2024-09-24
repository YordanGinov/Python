from collections import deque
chocolate = [int(el) for el in input().split(", ")]
cups_of_milk= deque([int(el) for el in input().split(", ")])
milkshakes_made = 0

while milkshakes_made < 5 and chocolate and cups_of_milk:
    if chocolate[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolate.pop()
        cups_of_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if cups_of_milk[0] == chocolate[-1]:
        cups_of_milk.popleft()
        chocolate.pop()
        milkshakes_made += 1
    else:
        cups_of_milk.rotate(-1)
        chocolate[-1] -= 5
if milkshakes_made >= 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
print(f'Chocolate: {", ".join([str(el) for el in chocolate]) if chocolate else "empty"}')
print(f"Milk: {', '.join([str(el) for el in cups_of_milk]) if cups_of_milk else 'empty'}")
