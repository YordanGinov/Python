class NotAnInt(Exception):
    pass
a = "k"
try:
    b = int(a)
except ValueError:
    raise NotAnInt("a is not an int")
else:
    print(b)