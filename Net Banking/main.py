# import all files in main 
from invalid_pin_error import InvalidPinError
from insufficient_balance_error import InsufficientBalanceError
from account import Account

# create object and call all arguments and parameters 

account1 = Account(1234,10000,123)

account2 = Account(5678,5000,321)

account1.check_balance(123)

#using correct pin
try:
    print(account1.check_balance(123))
except InvalidPinError:
    print("Pin is Wrong")

#for transfer balance
try:
    account1.transfer_balance(5678,2000,123)
except InvalidPinError:
    print("Pin is Wrong")
except InsufficientBalanceError:
    print("Balance is insufficient")


# static members can be accessed directly using class name

Account.bank_name

Account.calculate_emi(100000,1)

