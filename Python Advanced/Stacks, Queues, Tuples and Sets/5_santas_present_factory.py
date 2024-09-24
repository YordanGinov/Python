from collections import deque
materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])
presents_table = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic:
    if materials[-1] < 0 or magic[0] < 0:
        materials[-1] += magic[0]
        magic.popleft()
        continue
    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic[0] == 0:
        magic.popleft()
        continue
    current_material = materials.pop()
    current_magic = magic.popleft()
    if current_material*current_magic == 150:
        presents_table["Doll"] += 1
    elif current_material*current_magic == 250:
        presents_table["Wooden train"] += 1
    elif current_material*current_magic == 300:
        presents_table["Teddy bear"] += 1
    elif current_material*current_magic == 400:
        presents_table["Bicycle"] += 1
    elif current_material + current_magic > 0:
        materials.append(current_material + 15)

if (presents_table["Doll"] > 0 and presents_table["Wooden train"] > 0) or (presents_table["Teddy bear"] > 0 and presents_table["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(el) for el in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(el) for el in magic])}")
for present in sorted(presents_table.keys()):
    if presents_table[present] > 0:
        print(f"{present}: {presents_table[present]}")
