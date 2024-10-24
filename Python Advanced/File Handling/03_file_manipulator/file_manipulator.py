import os
text = None
while True:
    command = input()
    if command == 'End':
        break
    if len(command.split("-")) == 3:
        action, file_name, text = command.split("-")
    elif len(command.split("-")) == 4:
        action, file_name, old_string, new_string = command.split("-")
    else:
        action, file_name = command.split("-")

    if action == "Create":
        with open(f"./{file_name}", "w") as file:
            file.write("")
    elif action == "Add":
        with open(f"./{file_name}", "a") as file:
            file.write(text + "\n")
    elif action == "Replace":
        try:
            with open(f"./{file_name}") as file:
                lines = file.read()
            with open(f"./{file_name}", "w") as file:
                file.write("")
            for line in lines.split("\n"):
                if old_string in line:
                    line = line.replace(old_string, new_string)
                with open(f"./{file_name}", "a") as file:
                    file.write(line + '\n')
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(f"./{file_name}")
        except FileNotFoundError:
            print("An error occurred")