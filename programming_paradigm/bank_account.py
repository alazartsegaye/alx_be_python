class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        return f"Current balance: ${self.account_balance:.2f}"

if __name__ == "__main__":
    account = BankAccount(100)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()
