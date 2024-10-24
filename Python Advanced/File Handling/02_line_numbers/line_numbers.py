with open("../text.txt") as file:
    lines = file.read()
char_count = 0
punctuation_count = 0
current_line = 1
for line in lines.split("\n"):
    for char in line:
        if char.isalpha():
            char_count += 1
        else:
            punctuation_count += 1
    with open("./output.txt", "a") as f:
        f.write(f"Line {current_line}: {line}. ({punctuation_count})({char_count})" + '\n')
    char_count = 0
    punctuation_count = 0
    current_line += 1