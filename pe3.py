def encode(input, shift):
    letters = list('abcdefghijklmnopqrstuvwxyz')

    encode_text = []

    for char in input:
        if char.islower():
            index = letters.index(char)
            new_index = (index + shift) % 26
            encode_text.append(letters[new_index])
        else:
            encode_text.append(char)
    encode_text = ''.join(encode_text)
    return letters, encode_text

def decode(input, shift):
    letters = list('abcdefghijklmnopqrstuvwxyz')

    decode_text = []

    for char in input:
        if char.islower():
            index = letters.index(char)
            new_index = (index - shift) % 26
            decode_text.append(letters[new_index])
        else: decode_text.append(char)
    decode_text = ''.join(decode_text)
    return decode_text


import datetime

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be set in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return
        self.balance += amount
        print(f"Resulting Account Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative.")
            return
        self.balance -= amount
        print(f"Resulting Account Balance: ${self.balance}")
    
    def view_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            print("Withdrawals are only permitted after the account has been in existence for 180 days.")
            return
        if self.balance - amount < 0:
            print("Overdrafts are not permitted.")
            return
        super().withdraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30) 
            print(f"Overdrafts are permitted, but incur a $30 fee each time a withdrawal results in a negative balance. New balance: ${self.balance}")
        else:
            super().withdraw(amount)
