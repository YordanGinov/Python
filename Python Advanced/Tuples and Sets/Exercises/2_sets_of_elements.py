n, m = input().split()
set_one = set()
set_two = set()
for _ in range(int(n)):
    set_one.add(input())
for _ in range(int(m)):
    set_two.add(input())
intersection = set_one.intersection(set_two)
print('\n'.join(sorted(intersection)))
