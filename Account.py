from random import randint
from datetime import datetime

'''' 
transaction = {
    transaction_ID : ""
    type : "withdrawal | deposit | transfer"
    amount : 0
    date : ""
    account_Involved : ""

}

'''


class Account: 
    account_ID = ""
    account_number = ""
    account_type = ""
    account_name = ""
    id_card_number = ""
    account_balance = 0.0000
    transactions = []

    # Constructor
    def __init__(self, account_number, account_type, account_name, id_card_number): 
        self.account_ID = randint(1000, 9999)
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.id_card_number = id_card_number

    
    def __str__ (self): 
        return f''' 
            account_ID = {self.account_ID}
            account_number = {self.account_number}
            account_type = {self.account_type}
            account_name = {self.account_name}
            id_card_number = {self.id_card_number}
            account_balance = {self.account_balance}
        '''
    
    def deposit(self, amount, depositing_account): 

        self.account_balance += amount

        self.transaction(amount=amount, type="deposit", account_involved=depositing_account)


    def withdrawal (self, amount, withdrawing_agent): 

        if self.account_balance >= amount: 
            self.account_balance -= amount 

            self.transaction(amount=amount, type="withdrawal", account_involved= withdrawing_agent)
        else : 
            print("Insufficient Balance")

            
    def transaction (self, amount, account_involved, type): 
        trans_id = randint(1, 1000000)
        date = datetime.today()
        sign = "+"
        if type != "deposit": 
            sign = "-"

        trans = {
            "transaction_ID" : trans_id,
            "type ": type,
           " amount" : sign + str(amount),
            "date ": date,
            "account_Involved" : account_involved

        }

        self.transactions.append(trans)





acc1 = Account(account_type="normal",account_name= "John Doe",account_number= "112323", id_card_number="23448294")
print(acc1)

# Perform a deposit
acc1.deposit(amount=2000, depositing_account="12324")


print("-------------------------------------")
print(acc1)

acc1.withdrawal(amount= 1500, withdrawing_agent= "123423")
print("-------------------------------------")
print(acc1)
print(acc1.transactions)