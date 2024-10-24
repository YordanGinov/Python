def list_roman_emperors(*arg, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    for index in range(len(arg)):
        name = arg[index][0]
        if arg[index][1] is True:
            if name not in successful_emperors:
                successful_emperors[name] = 0
                if name in kwargs:
                    successful_emperors[name] = kwargs[name]
        elif arg[index][1] is False:
            if name not in unsuccessful_emperors:
                unsuccessful_emperors[name] = 0
                if name in kwargs:
                    unsuccessful_emperors[name] = kwargs[name]
    sorted_successful_emperors = sorted(successful_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    sorted_unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))
    result = f"Total number of emperors: {len(arg)}\n"
    if sorted_successful_emperors:
        result += f"Successful emperors:\n"
        for name, age in sorted_successful_emperors:
            result += f"****{name}: {age}\n"
    if sorted_unsuccessful_emperors:
        result += f"Unsuccessful emperors:\n"
        for name, age in sorted_unsuccessful_emperors:
            result += f"****{name}: {age}\n"
    return result
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))