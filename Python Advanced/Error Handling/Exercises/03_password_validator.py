class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARS = ["@", "*", "&", "%"]
MIN_PWD_LEN = 8

while True:
    password = input()
    if password == "Done":
        break

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if len(password) < MIN_PWD_LEN:
        raise(PasswordTooShortError("Password must contain at least 8 characters"))

    if password.isalpha() or password.isdigit() or all(char in SPECIAL_CHARS for char in password):
        raise(PasswordTooCommonError("Password must be a combination of digits, letters, and special characters"))

    if not any(char in password for char in SPECIAL_CHARS):
        raise(PasswordNoSpecialCharactersError("Password must contain at least 1 special character"))

    print("Password is valid")
