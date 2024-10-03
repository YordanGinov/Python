class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

MIN_NAME_LEN = 5
TLD_NAMES = ["com", "bg", "org", "net"]

while True:
    user_input = input()
    if user_input == 'End':
        break

    if '@' not in user_input:
        raise MustContainAtSymbolError('Email must contain @')

    user_name, domain = user_input.split('@')

    if len(user_name) < MIN_NAME_LEN:
        raise NameTooShortError('Name must be more than 4 characters')

    _, tld = domain.split('.')
    if tld not in TLD_NAMES:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print("Email is valid")