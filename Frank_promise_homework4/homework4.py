"""
1. we will use exception handling to simulate withdraws
2. users will be prompted for an input:
   user: inputs a number
   input cannot be blank
   if the user inputs strings raise an error
   if the user enters a number not in the database, raise an error
3. If the user is able to move forward, then the user should be prompted for another input
   user: input an amount should be between 1 and 100 dollars
   input cannot be blank

   if user tries to withdraw more than 100 dollars, raise an error
   if the user inputs a string, raise an error

4. we find a way to deduct the amount

5. send a notification to the user if transaction is successful.
6. send a notification in case of any error

"""

user = {'Pin': 12345,
        'balance': 100

        }


class InvalidPinCodeError(Exception):
    pass


def validate_pin_code(number):

    if number != user['Pin']:

        raise InvalidPinCodeError("Invalid pin")


def validate_cash_withdrawal(amount):
    if amount > user['balance']:
        raise ValueError("Insufficient funds")


def withdraw_cash():
    pin_count_trials = 0
    max_trials = 3
    while pin_count_trials < max_trials:
        pin_count_trials += 1
        pin = int(input("Input your pin: "))
        try:
            validate_pin_code(pin)
        except InvalidPinCodeError:
            print(f"Wrong pincode. {max_trials - pin_count_trials} trial(s) left")
        else:
            break

        if pin_count_trials == max_trials:
            print("Your card has been blocked")
            exit()

    def operation():
        try:
            amount = int(input("cash withdraw: "))
            if amount % 10 != 0:
                return "Sorry you can only withdraw in increments of 10"

            else:
                validate_cash_withdrawal(amount=amount)

                user['balance'] = user['balance'] - amount
                return f"{amount} dollars  successfully withdrawn. Your remaining balance is {user['balance']} dollars"

        except ValueError:

            return f"Insufficient fund. Your account balance is {user['balance']} dollars."

    acceptable_values = ("y", "n")
    continue_operation = "y"

    while continue_operation == "y":
        print(operation())

        continue_operation = input("Do you want to continue [Y/N] ").lower()
        if continue_operation not in acceptable_values:
            print("Unknown input")
    else:
        exit()


withdraw_cash()


