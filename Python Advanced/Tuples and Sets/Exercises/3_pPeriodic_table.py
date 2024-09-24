n = int(input())
chemicals = set()
for _ in range(n):
    chemical_compound = input().split()
    for chemical in chemical_compound:
        chemicals.add(chemical)
print('\n'.join(chemicals))
