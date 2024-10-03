class MoneyNotEnoughError(Exception):
    pass
class PINCodeError(Exception):
    pass
class UnderageTransactionError(Exception):
    pass
class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = [int(data) for data in input().split(', ')]
if balance < 0:
    raise MoneyIsNegativeError("The amount of money cannot be a negative number")

while True:
    command = input()
    if command == "End":
        break
    try:
        action, money, pin_code = command.split('#')
    except ValueError:
        action, money = command.split('#')
        pin_code = ''
    try:
        money = int(money)
    except ValueError:
        print("Money must be a whole number.")
    if pin_code != '':
        try:
            pin_code = int(pin_code)
        except ValueError:
            print("Pin code must be a whole number.")
    if action == "Send Money":
        if balance < money:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        elif pin_code != pin:
            raise PINCodeError("Invalid Pin code")
        elif age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")
    elif action == "Receive Money":
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance += money / 2
        print(f"{money/2:.2f} money went straight into the bank account")