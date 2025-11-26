from hypothesis.stateful import RuleBasedStateMachine, rule, precondition, invariant
from hypothesis import strategies as st
from bank import BankAccount


class BankMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.model_balance = 0     # modelul nostru (asteptat)
        self.sut = BankAccount()   # System Under Test

    @rule(amount=st.integers(min_value=0, max_value=10_000))
    def deposit(self, amount):
        self.sut.deposit(amount)
        self.model_balance += amount

    @precondition(lambda self: self.model_balance > 0)
    @rule(amount=st.integers(min_value=0, max_value=10_000))
    def withdraw(self, amount):
        # dacă amount > balance, ne așteptăm la excepție
        if amount > self.model_balance:
            try:
                self.sut.withdraw(amount)
            except ValueError:
                pass
            else:
                assert False, "Expected ValueError for overdraft"
        else:
            self.sut.withdraw(amount)
            self.model_balance -= amount

    @invariant()
    def balances_match(self):
        assert self.sut.balance() == self.model_balance


TestBank = BankMachine.TestCase
