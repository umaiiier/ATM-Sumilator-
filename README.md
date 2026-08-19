# 🏦 Python ATM Simulator

A simple **ATM Simulator** built using Python. This beginner-friendly project allows users to perform basic banking operations through the command line.

## ✨ Features

* 🔐 PIN Authentication
* 💰 Check Account Balance
* 💸 Withdraw Money
* 💵 Deposit Money
* 🔄 Change PIN
* ❌ Invalid PIN Handling
* ⚠️ Insufficient Balance Check
* 🔒 PIN Confirmation when changing PIN

## 🛠️ Technologies Used

* Python 3

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

1. Check balance
2. Withdraw
3. Deposit
4. Change PIN

Enter your choice: 4

Enter your new PIN: 456
Confirm your new PIN: 456

PIN changed successfully!
```

## 📖 How It Works

1. User enters their PIN.
2. The program verifies the PIN.
3. If the PIN is correct, an ATM menu is displayed.
4. The user can:

   * Check their balance
   * Withdraw money
   * Deposit money
   * Change their PIN
5. When changing the PIN, the user must enter and confirm the new PIN.
6. If both PINs match, the PIN is changed.
7. The balance is updated after withdrawals and deposits.

## 🎯 Learning Objectives

This project helps beginners practice:

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* Basic Arithmetic
* Comparison Operators
* Updating Variables
* PIN Validation
* Console-based Programs

## 🔮 Future Improvements

* Multiple user accounts
* Transaction history
* Receipt generation
* Data storage using files or databases
* Retry limit for incorrect PIN
* Better menu using loops
* Permanent PIN storage

## 👨‍💻 Author

**Umair Naseer**
