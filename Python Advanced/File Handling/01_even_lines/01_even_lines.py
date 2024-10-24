REPLACE_SYMBOLS = ['-', ',', '.', '!', '?']
with open("../text.txt") as file:
    lines = file.read()
for line in lines.split("\n"):
    for char in line:
        if char in REPLACE_SYMBOLS:
            line = line.replace(char, "@")
    reversed_text = line.split()
    for index in range(len(reversed_text) -1, -1, -1):
        print(reversed_text[index], end=' ')
    print()