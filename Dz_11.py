# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

import time
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OperationName(Enum):
    PLUS = "Replenishment"
    MINUS = "Withdrawal"


class BankAcc:

    def __init__(self):
        self.balance = 0
        self.history = []


    def replenishment_of_the_balance(self, amount: int):
        self.amount = amount
        time.sleep(1)
        self.balance += self.amount
        self.history.append(BankAccountHistory(amount, OperationName.PLUS, datetime.now()))

    def withdrawals(self, amount: int):
        self.amount = amount
        time.sleep(1)
        self.balance -= self.amount
        self.history.append(BankAccountHistory(amount, OperationName.MINUS, datetime.now()))


@dataclass
class BankAccountHistory:
    amount: int
    operation: OperationName
    date_time: datetime


account_Nick = BankAcc()

account_Nick.replenishment_of_the_balance(10)
print(account_Nick.balance)
account_Nick.replenishment_of_the_balance(30)
print(account_Nick.balance)
account_Nick.withdrawals(12)
print(account_Nick.balance)
print(account_Nick.history)

account_Mick = BankAcc()

account_Mick.replenishment_of_the_balance(100)
print(account_Mick.balance)
account_Mick.withdrawals(10)
print(account_Mick.balance)
account_Mick.replenishment_of_the_balance(360)
print(account_Mick.balance)
print(account_Mick.history)


