class BankAccount:

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise AccountOperationError(ValueError, initial_balance)
        self._balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise AccountOperationError(amount)

        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise AccountOperationError(amount)

        if amount > self._balance:
            raise AccountOperationError(amount, operation="withdraw")

        self._balance -= amount

    @property
    def balance(self):
        return self._balance

class AccountOperationError(Exception):

    def __init__(self, value, operation=None):
        self.operation = operation
        self.value = value

    def __str__(self):
        if self.operation == 'withdraw':
            return "Запрошенная сумма больше текущего баланса"
        return f"Вы ввели отрицательное число. Значение: '{self.value}'"


acc = BankAccount(2)
acc.deposit(15)
acc.withdraw(2)
acc.withdraw(-2)
