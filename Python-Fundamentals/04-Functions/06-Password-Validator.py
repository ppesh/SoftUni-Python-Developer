# 06. Password Validator

def validate_password(password):
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for element in password:
        if not element.isdigit() and not element.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    count_digits = 0
    for element in password:
        if element.isdigit():
            count_digits += 1

    if count_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
valid_res = validate_password(password)

if valid_res:
    print("Password is valid")
