# Bank Management System

---

## Contents
- Overview
- Design Philosophy
- Class Breakdown
  - Bank Class
  - Account Class
  - Coin Collector Class
- Program Flow
- Transactions Permitted
- Input Validation
- Test Cases

---

## Overview

This program simulates a simple bank management application. The goal was to build something that can perform the same kinds of transactions a user might need in a basic banking system.

You can:
- Open accounts  
- View account information  
- Change PINs  
- Deposit and withdraw money  
- Transfer funds between accounts  
- Deposit coins  
- Close accounts  
- Exit the program  

The program now also persists account data between runs using JSON.

---

## Design Philosophy

This project makes heavy use of Object Oriented Programming, specifically:
- Encapsulation  
- Abstraction  

I also focused heavily on input validation and edge cases. At every step, inputs are checked and either corrected or safely rejected without crashing the program.

A big goal was **minimal responsibility**:
- Each function and method does one job  
- Repeated logic is pushed into helper functions  
- The main driver acts more like a controller than a worker  

I also started developing my own coding style here. You’ll see mostly `snake_case`, though some naming originally followed different conventions. That’s been cleaned up during refactoring.

---

## Class Breakdown

### Bank Class

Represents the bank itself.

- Holds a list of accounts (`account_list`)
- Uses a constant (`SUPPORTED_ACCOUNTS`) to define max capacity
- Provides:
  - `add_account_to_bank`
  - `remove_account_from_bank`
  - `find_account`

The class is intentionally simple — it mainly acts as a container and interface for account objects.

---

### Account Class

Represents an individual bank account.

Core methods:
- `deposit`
- `withdraw`
- `is_valid_pin`

The `withdraw` method also handles insufficient funds, which slightly breaks the “single responsibility” idea, but reduces repeated checks elsewhere.

The `__str__` method formats account information cleanly for printing.

---

### CoinCollector Class

Handles coin-based deposits.

- Accepts a string input of coin codes  
- Each character represents a coin type:

  - P = Penny ($0.01)  
  - N = Nickel ($0.05)  
  - D = Dime ($0.10)  
  - Q = Quarter ($0.25)  
  - H = Half Dollar ($0.50)  
  - W = Whole Dollar ($1.00)  

Example input: PNDQW  
This would be parsed as 1 Penny, 1 Nickel, 1 Dime, 1 Quarter, and 1 Dollar.

The class:
- Counts valid coins  
- Tracks invalid characters separately  
- Converts totals into a dollar amount using a helper method (`calculate_amount`)  

Any characters that do not match a valid coin code are stored and reported back to the user.

This class is created only when needed and discarded after use.

---

## Program Flow

Execution begins in `bank_manager()`.

- A `Bank` object is created
- Stored accounts are loaded from a JSON file
- The main loop runs until the user exits

The loop:
- Displays a menu
- Validates input
- Routes execution to the correct operation

The main function acts mostly as a **controller**, delegating work to:
- Classes
- Helper functions
- Input handlers

### Notable Case: ATM Withdrawal

ATM withdrawals required extra handling:
- Must be multiples of $5
- Must not exceed balance
- Must retry on invalid input

To handle this, I track the previous balance and loop until a valid withdrawal occurs or the user exits.

It’s not the cleanest solution, but it works reliably.

---

## Transactions Permitted

The system supports:
- Deposits  
- Withdrawals  
- Transfers between accounts  
- Coin deposits  
- ATM-style withdrawals  

---

## Input Validation

All user input is validated through helper functions.

This avoids:
- Repeated validation logic
- Crashes from bad input

Invalid inputs:
- Prompt retry when appropriate  
- Fail safely otherwise  

---

## Test Cases

I tested a range of edge cases to make sure the system behaves correctly:

- Rejecting zero-value transactions  
- Preventing overdrafts  
- Handling invalid PINs and account numbers  
- Ensuring account limits work correctly  
- Verifying account deletion  
- Enforcing ATM withdrawal rules (multiples of 5, limits, etc.)  
- Preventing crashes from bad menu input  
- Fixing a bug where invalid input reused previous selections  
- Fixing transfer logic so failed transfers don’t still update balances  

---

## Notes

This project was later refactored into a modular structure:

- Separate modules for accounts, bank logic, input handling, and storage  
- JSON-based persistence (`accounts.json`)  
- Cleaner naming and structure  

---

## Future Improvements

- Replace fixed-size account list with dynamic storage  
- Improve ATM withdrawal logic structure  
- Add better separation between UI and logic  
- Potential move to a simple API or GUI  

---

## Running the Program

```bash
python main.py