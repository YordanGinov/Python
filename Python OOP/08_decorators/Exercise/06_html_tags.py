def tags(data_type):
    def wrapper(func):
        def decorator(*args):
            return f"<{data_type}>{func(*args)}</{data_type}>"
        return decorator
    return wrapper

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
