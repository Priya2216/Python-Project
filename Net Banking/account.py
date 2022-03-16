from invalid_pin_error import InvalidPinError
from insufficient_balance_error import InsufficientBalanceError
from datetime import datetime as dt


class Account:
    
    bank_name="ITVBank"
    
    def __init__(self,account_number,balance,pin):
        
        self.__account_number = account_number
        self.__balance = balance
        self.__pin = pin
        
        file = open(str(account_number)+".txt","x")
        file.close()

# Function for check balance        
    def check_balance(self,pin):
        
        if pin == self.__pin:
            
            #file code
            file = open(str(self.__account_number)+".txt","a")
            file.write("check balance at - {} \n ".format(dt.now()))
            file.flush()
            file.close()
            
            return self.__balance
        else:
            raise InvalidPinError
                  
            
# __ before oin balance to make things privtae 
# so without pin it is not possible to access he information

# Function for transfer balance 
    def transfer_balance(self,other,amount,pin):
        
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                other.__balance += amount
                   
                file = open(str(self.__account_number)+".txt","a")
                file.write("fund transfer at - {}, to account - {} ,closing balance - {} \n" .format(dt.now(),other.__account_number, self.__balance))
                file.flush()
                file.close()
                   
                file = open(str(other.__account_number)+".txt","a")
                file.write("fund recieved at - {} ,from account - {}, closing balance - {} \n" .format(dt.now(),self.__account_number, other.__balance))
                file.flush()
                file.close()
            else:
                raise InsufficientBalanceError
                
        else:
            raise InvalidPinError
            
            
# Function for EMI    
    @staticmethod 
    def calculate_emi(loan_amount,year):
         
         months = year* 12
         monthly_emi = loan_amount/months
         return monthly_emi
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     