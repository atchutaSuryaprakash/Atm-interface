import datetime

class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            self.current_user = user
            print("Login successful.")
        else:
            print("Invalid user ID or pin.")
            self.current_user = None

    def show_menu(self):
        print("\n1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.current_user.transactions:
            print(transaction)

    def withdraw(self):
        amount = float(input("\nEnter amount to withdraw: "))
        if amount > self.current_user.balance:
            print("Insufficient funds.")
        else:
            self.current_user.balance -= amount
            transaction = f"{datetime.datetime.now()} - Withdraw: ${amount:.2f}"
            self.current_user.add_transaction(transaction)
            print(f"${amount:.2f} withdrawn successfully.")

    def deposit(self):
        amount = float(input("\nEnter amount to deposit: "))
        self.current_user.balance += amount
        transaction = f"{datetime.datetime.now()} - Deposit: ${amount:.2f}"
        self.current_user.add_transaction(transaction)
        print(f"${amount:.2f} deposited successfully.")

    def transfer(self):
        recipient_id = input("\nEnter recipient user ID: ")
        recipient = self.users.get(recipient_id)
        if not recipient:
            print("Recipient user ID not found.")
            return
        amount = float(input("Enter amount to transfer: "))
        if amount > self.current_user.balance:
            print("Insufficient funds.")
        else:
            self.current_user.balance -= amount
            recipient.balance += amount
            transaction = f"{datetime.datetime.now()} - Transfer to {recipient_id}: ${amount:.2f}"
            self.current_user.add_transaction(transaction)
            recipient_transaction = f"{datetime.datetime.now()} - Transfer from {self.current_user.user_id}: ${amount:.2f}"
            recipient.add_transaction(recipient_transaction)
            print(f"${amount:.2f} transferred successfully to user {recipient_id}.")

    def quit(self):
        print("Thank you for using the ATM.")
        self.current_user = None

def main():
    atm = ATM()

    # Adding some users
    user1 = User(user_id="user1", pin="1234", balance=1000)
    user2 = User(user_id="user2", pin="5678", balance=2000)
    atm.add_user(user1)
    atm.add_user(user2)

    while True:
        user_id = input("Enter user ID: ")
        pin = input("Enter pin: ")
        atm.authenticate_user(user_id, pin)
        if atm.current_user:
            while True:
                atm.show_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    atm.transaction_history()
                elif choice == '2':
                    atm.withdraw()
                elif choice == '3':
                    atm.deposit()
                elif choice == '4':
                    atm.transfer()
                elif choice == '5':
                    atm.quit()
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
