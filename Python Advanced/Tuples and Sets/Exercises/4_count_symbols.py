text = tuple(input())
occ = {}
for char in text:
    if char not in occ:
        occ[char] = 1
    else:
        occ[char] += 1

for occurrence in sorted(occ):
    print(f'{occurrence}: {occ[occurrence]} time/s')
