class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount: int):
        assert amount >= 0
        self._balance += amount

    def withdraw(self, amount: int):
        assert amount >= 0
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def balance(self) -> int:
        return self._balance
