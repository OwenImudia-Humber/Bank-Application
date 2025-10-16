# Bank-Application
A simple command-line bank application built in Python. Users can log in using a 4-digit PIN, check their balance, make deposits or withdrawals, and exit securely. Includes input validation and limited PIN attempts.

🧠 Features

✅ 3 login attempts using a 4-digit PIN before exit
✅ Displays balance with two decimal places
✅ Supports withdrawals with preset or custom amounts
✅ Validates funds before allowing withdrawals
✅ Supports deposits with preset or custom amounts
✅ Fully menu-driven system
✅ Built entirely using Python functions
✅ Handles invalid inputs gracefully

🧮 Menu Options

Display Balance — Shows your current account balance.

Make a Withdrawal — Choose a preset or custom amount. Ensures you have enough funds.

Make a Deposit — Choose a preset or custom amount to add to your balance.

Exit — Ends the program.

🔐 Login System

You start by entering a 4-digit PIN.

You get 3 attempts before the program exits automatically.

Once authenticated, you’re welcomed into the main menu.

🖥️ Example Run
-----WELCOME TO DUB BANK-----
Enter a 4-digit PIN: 1234
Welcome in :)

-----MAIN MENU-----
1. Display the balance
2. Make a withdrawal
3. Make a deposit
4. Exit
What choice would you like to make: 2

*****WITHDRAWAL******
-----Pick a choice-----
1. $20
2. $40
3. $60
4. $80
5. $100
6. Custom amount
What would you like to do? 1
New balance: $480.00

⚙️ How to Run

Make sure you have Python 3 installed.

Clone this repository:

git clone (https://github.com/OwenImudia-Humber/Bank-Application.git)


Navigate to the project folder:

cd Mini-P_Owenimudia.py 


Run the program:

python Mini-P_Owenimudia.py 

🧩 File Structure
📦 Lab-Six/
 ┣ 📜 Mini-P_OwenImudia.py     # Main Python file
 ┣ 📁 .idea/                   # PyCharm config (optional to ignore)
 ┣ 📜 .gitignore               # Files to exclude from Git tracking
 ┣ 📜 README.md                # Project documentation


📚 Skills Demonstrated

Python functions and modular design

Input validation and exception handling

Loops and conditionals

Simple user authentication logic

Command-line UI design

🧑‍💻 Author

Owen Imudia
📧 Imudiaowen@gmail.com
