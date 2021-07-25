def tags(html_tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{html_tag}>{func(*args)}</{html_tag}>"

        return wrapper

    return decorator


# Test Code
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))