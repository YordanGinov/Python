def type_check(data_type):
    def wrapper(func):
        def decorator(data):
            if isinstance(data, data_type):
                return func(data)
            return "Bad Type"
        return decorator
    return wrapper




@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
