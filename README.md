# 🏦 Python ATM Simulator

A simple **ATM Simulator** built using Python. This beginner-friendly project allows users to perform basic banking operations through the command line.

## ✨ Features

* 🔐 PIN Authentication
* 💰 Check Account Balance
* 💸 Withdraw Money
* 💵 Deposit Money
* ❌ Invalid PIN Handling
* ⚠️ Insufficient Balance Check
* ⚠️ Invalid Menu Choice Handling

## 🛠️ Technologies Used

* Python 3
* `input()`
* `print()`
* `if`, `elif`, `else`
* Comparison operators
* Arithmetic operators
* f-strings

## 📂 Project Structure

```text
ATM-Simulator/
│── atm.py
│── README.md
```

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python atm.py
```

## 📝 Example

```text
Welcome to the ATM

Enter your PIN: 123

Welcome to your account

________ What would you like to do? ________

1. Check balance
2. Withdraw
3. Deposit

Enter your choice: 1

Your balance is: 1000
```

## 📖 How It Works

1. User enters the PIN.
2. The program verifies the PIN.
3. If the PIN is correct, an ATM menu is displayed.
4. The user selects an operation:

   * Check balance
   * Withdraw money
   * Deposit money
5. For withdrawals, the program checks whether sufficient funds are available.
6. The balance is updated after a successful transaction.
7. The program displays an appropriate message for invalid choices or insufficient funds.

## 🎯 Learning Objectives

This project helps beginners practice:

* Variables
* User input using `input()`
* Output using `print()`
* `int` data type
* Conditional statements (`if`, `elif`, `else`)
* Comparison operators
* Arithmetic operators
* Assignment operators (`+=`, `-=`)
* f-strings
* Nested conditional statements
* Basic decision-making logic
* Console-based programming

## 🔮 Future Improvements

* Add a `while` loop for multiple transactions
* Add an Exit option
* Add input validation
* Add a retry limit for incorrect PIN attempts
* Add a Change PIN feature
* Add multiple user accounts
* Add transaction history
* Add receipt generation
* Store account data using files
* Add database support
* Use functions to organize the program
* Build a graphical user interface (GUI)

## 👨‍💻 Author

**Umair Naseer**

BSCS Student | Learning C++ & Python
