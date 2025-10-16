def display_balance(balance):
    print(f"Your balance is: ${balance:.2f}")


def make_withdrawal(balance):
    while True:
        print("*****WITHDRAWAL******\n"
              "-----Pick a choice-----\n"
              "1. $20\n"
              "2. $40\n"
              "3. $60\n"
              "4. $80\n"
              "5. $100\n"
              "6. Custom amount\n")
        try:
            choice = int(input("What would you like to do?  "))

            if choice == 1:
                amount = 20
            elif choice == 2:
                amount = 40
            elif choice == 3:
                amount = 60
            elif choice == 4:
                amount = 80
            elif choice == 5:
                amount = 100
            elif choice == 6:
                amount = float(input("Enter custom amount: $"))
                if amount < 0:
                    print("Amount must be greater than 0")
                    continue
            else:
                print("Invalid choice.")
                continue

            if amount > balance:
                print("Insufficient funds. Please try again.")
                continue

            balance -= amount
            print(f"New balance: ${balance:.2f}")
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    return balance


def make_deposit(balance):
    while True:
        print("*****DEPOSIT******\n"
              "-----Pick a choice-----\n"
              "1. $20\n"
              "2. $40\n"
              "3. $60\n"
              "4. $80\n"
              "5. $100\n"
              "6. Custom amount\n")

        try:
            amount = int(input("What would you like to do?  "))
            if amount == 1:
                balance += 20
            elif amount == 2:
                balance += 40
            elif amount == 3:
                balance += 60
            elif amount == 4:
                balance += 80
            elif amount == 5:
                balance += 100
            elif amount == 6:
                custom_amount = float(input("How much would you like to deposit? $"))
                if custom_amount < 0:
                    print("Amount must be greater than 0")
                    continue
                balance += custom_amount
            else:
                print("Invalid choice. Please enter a number between 1 and 6")
                return balance

            print(f"New balance: ${balance:.2f}")

            break
        except ValueError:
            print("Invalid input please enter a number")

    return balance


def login():
    password = 1234
    tries = 0
    print("-----WELCOME TO DUB BANK-----")
    while tries < 3:

        pin_result = int(input("Enter a 4-digit PIN: "))

        if len(str(pin_result)) !=4:
            print("The input has to be 4 digits")
            continue

        if pin_result == password:
            print("Welcome in :)")
            return True
        else:
            print("The PIN is wrong.")
            tries += 1

    print("Too many incorrect attempts. Exiting...")
    return False

def display_main_menu():
    while True:
        print("\n-----MAIN MENU-----")
        print("1. Display the balance")
        print("2. Make a withdrawal")
        print("3. Make a deposit")
        print("4. Exit")
        try:
            choice = int(input("What choice would you like to make: "))
            if choice >= 1 and choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4")
        except ValueError:
            print("Invalid input. Enter a number")

def main():
    if not login():
        return

    balance = 500.00

    while True:
        choice = display_main_menu()

        if choice == 1:
            display_balance(balance)
        elif choice == 2:
            balance = make_withdrawal(balance)
        elif choice == 3:
            balance = make_deposit(balance)
        elif choice == 4:
            print("Thank you for using Humber Bank!")
            break

if __name__ == "__main__":
    main()
