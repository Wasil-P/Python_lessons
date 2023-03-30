# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from datetime import datetime

class BankAcc:

    def __init__(self):
        self.balance = 0
        self.last_operation = ()


    def replenishment_of_the_balance(self, summa_currency: int):
        self.summa_currency = summa_currency
        self.balance += self.summa_currency
        self.last_operation = (f"Replenishment of the balance {self.balance} {datetime.now()}")

    def withdrawals(self, summa_currency: int):
        self.summa_currency = summa_currency
        self.balance -= self.summa_currency
        self.last_operation = (f"Withdrawal of funds from the balance {self.balance} {datetime.now()}")

    def last_operation(self):
        print(self.last_operation)

class OperationsHistory:

    def __init__(self):
        self.last_operation_history = BankAcc()


    def show_last_tansactions(self):
        print(last_operation_history.last_operation)


last_operation_history = BankAcc()

account_Nick = BankAcc()
operations_Nick = OperationsHistory()

account_Nick.replenishment_of_the_balance(10)
print(account_Nick.balance)
account_Nick.replenishment_of_the_balance(50)
print(account_Nick.balance)
account_Nick.withdrawals(12)
print(account_Nick.balance)

print(last_operation_history.last_operation)


