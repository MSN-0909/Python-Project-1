from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    # Create a new user with name and email
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    user = User(name, email)
    
    # Validate email format
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return  # Exit the function if the email is invalid
    
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    # List all users
    if not users:
        print("No users available.")
        return
    for i, user in enumerate(users):
        print(f"{i + 1}. {user}")

def create_account():
    # Ensure there are users before creating an account
    if len(users) == 0:
        print("No users found. Please create a user first.")
        return
    
    list_users()
    idx = int(input("Select user number: ")) - 1
    
    # Handle invalid user selection
    if idx < 0 or idx >= len(users):
        print("Invalid user selection.")
        return
    
    print("Account Type:")
    print("1. Savings Account")
    print("2. Student Account")
    print("3. Current Account")
    
    # Input validation for account type
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        if account_choice not in [1, 2, 3]:
            print("Invalid account choice! Defaulting to BankAccount.")
            account_choice = 0  # Default to BankAccount if invalid
    except ValueError:
        print("Invalid input! Defaulting to BankAccount.")
        account_choice = 0  # Default to BankAccount on non-integer input
    
    amount = float(input("Enter initial deposit: "))
    
    # Create account based on choice
    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        account = BankAccount(amount)
    
    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    
    # Show user's account balances
    for i, acc in enumerate(user.accounts):
        print(f"{i + 1}. Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    
    # Validate account selection
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selection.")
        return
    
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        user.accounts[acc_idx].deposit(amount)
        print(f"Rs. {amount} deposited successfully.\n")
    except ValueError:
        print("Invalid deposit amount.")

def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    
    # Show user's account balances
    for i, acc in enumerate(user.accounts):
        print(f"{i + 1}. Balance: Rs. {acc.get_balance()}")
    
    acc_idx = int(input("Select account: ")) - 1
    
    # Validate account selection
    if acc_idx < 0 or acc_idx >= len(user.accounts):
        print("Invalid account selection.")
        return
    
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        user.accounts[acc_idx].withdraw(amount)
        print(f"Rs. {amount} withdrawn successfully.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    
    # Display account balances and transaction history
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i + 1} - Balance: Rs. {acc.get_balance()}")
        print("Transactions:")
        for tx in acc.get_transaction_history():
            print(tx)
        print("-" * 20)  # Separator between accounts

