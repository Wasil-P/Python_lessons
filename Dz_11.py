# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from dataclasses import dataclass
from datetime import datetime

class BankAcc:

    def __init__(self):
        self.balance = 0
        self.history: list[BankAccountHistory] = []


    def replenishment_of_the_balance(self, summa_currency: int):
        self.summa_currency = summa_currency
        time.sleep(1)
        self.balance += self.summa_currency
        self.history.append([(f"Replenishment of the balance {self.balance} {datetime.now()}")])

    def withdrawals(self, summa_currency: int):
        self.summa_currency = summa_currency
        time.sleep(1)
        self.balance -= self.summa_currency
        self.history.append([(f"Withdrawal of funds from the balance {self.balance} {datetime.now()}")])


@dataclass
class BankAccountHistory:
    history: list


account_Nick = BankAcc()
operations_Nick = BankAccountHistory(account_Nick.history)

account_Nick.replenishment_of_the_balance(10)
print(account_Nick.balance)
account_Nick.replenishment_of_the_balance(30)
print(account_Nick.balance)
account_Nick.withdrawals(12)
print(account_Nick.balance)
print(operations_Nick.history)

account_Mick = BankAcc()
operations_Mick = BankAccountHistory(account_Mick.history)

account_Mick.replenishment_of_the_balance(100)
print(account_Mick.balance)
account_Mick.withdrawals(110)
print(account_Mick.balance)
account_Mick.replenishment_of_the_balance(360)
print(account_Mick.balance)
print(operations_Mick.history)


