def type_check(type_of_param):
    def decorator(func):
        def wrapper(param):
            if type(param) == type_of_param:
                return func(param)
            return f"Bad Type"

        return wrapper

    return decorator


# Test Code
@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))