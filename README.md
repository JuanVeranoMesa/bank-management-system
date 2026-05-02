========================
Bank Management System
========================

Contents:
0. Disclaimer
1. Overview
2. Design philosophy
3. Class Breakdown
3A. Bank Class
3B. Account Class
3C. Coin Collector Class
4. Program Flow
5. Transactions permitted
6. Input validation
7. Test cases

========================
0. Disclaimer
This is my pure-text submission for this program. My original README was made with the skeleton of the provided source HTM manual in a very old PC game I own. In case using an HTM skeleton from a copyrighted/external source is not allowed, this exists as a replacement.

========================
1. Overview

This program is meant to simulate a bank management application. I focused on making a program that can perform the same transactions a customer may need. I followed all guidelines stated by the provided final project pdf instructions in the creation of this program. This means the program allows you to open accounts, get information, change balances, change pin, transfer balances, and close accounts. It also allows you to end the program, of course.

========================
2. Design philosophy

This project makes heavy used of two Object Oriented Programming (OOP) paradigms. Throughout the code, you will see Classes that use: Encapsulation, Abstraction.  Additionally, I built checks in at every step to ensure edge cases (incorrect inputs, out of range inputs) are accounted for and either provide an option to fix (preferred)  or don't affect the program negatively such as crashing.

All of my classes and functions were created with "minimal responsibility" in mind. In order to reduce repeated code or to reduce amount of jobs each function, method, and class would have to take care of, I would often delegate steps to helper functions.

I imported the random library to aid in creation of various random numbers throughout the program. Additionally, I am working on developing my own "coding voice" and part of it was the adoption of "snake_case" naming schemes. This program contains a mix of both "camelCase" and "snake_case" variable and function names because I made sure to exactly follow the instructions for required functions and variables which defaulted to the former formatting style. I recognize this is a mix of styles, but I am confident establishing a personal, consistent guideline would be allowed for the project.

========================
3. Class Breakdown

3A Bank class:
This is class represents a bank, obviously. As per class instructions, it contains three methods. It also contains a list of accounts, and a constant representing the number of allowed accounts.

The opening of the bank class establishes the constant called "SUPPORTED_ACCOUNTS", which is in all-caps following PEP-8 guidelines. This constant is the same for all bank objects that may be created (even though, of course, this program only ever creates one such object). It is immediately used in the class constructor to create the "account_list" of SUPPORTED_ACCOUNTS length, where each value is None. This is what defines how many accounts are allowed, and a list which is often used when searching for accounts.

The functions "addAccountToBank", "removeAccountFromBank" and "findAccount" are often used to facilitate exactly what their names state. From these, findAccount is very important as it is called for the "promptForAccountNumberAndPin", which itself is called by most actions performed by the program. These three follow identical structure: They use an index "i" to loop through the list of accounts in order to perform their designated functions (set empty index to account object for the first, set matching account object to None for the second, and return the account object based on its account number for the third).

I made sure that bank itself had minimal methods and was as tight as possible. It really had only four jobs, to make hold the account objects, and three ways to interact with the account objects.


3B Account class:
This is a class that represents an account and the required methods for said account. These were relatively simple. I had the "deposit", "withdraw", "isValidPIN" methods as required by the instructions. These had simple jobs, exactly as written by their names, with the only one having a "dual" job being "withdraw" since I found that it being the closest function to an account's balance meant it could be universally used to also check if what you withdraw is too much and print a universal error to the user. This is one of the few times I break the "minimal responsibility" clause within methods, and I feel it is acceptable as it reduces code repetition.

The dunder method "__str__" was also defined for this class as per the instructions. I followed the example output exactly, and simply stated each of the stored information points. The SSN was obscured to only output the last four digits using string slicing. No actual printing was done here, and instead a string was added on to with each piece of information and then returned, allowing for a direct "print(account)" call.


3C CoinCollector class:
This is a class that represented a coin counter and its methods. I had a bit more freedom with how to set the class up and decided that it only ever exist for a single main driver option--that's to say, it would be created, used and then "discarded" when option 8 was selected. In reality, option 8 simply initializes a new object and stores it in a temporary variable when chosen so it's more akin to overwriting (the object previous may still exist somewhere in memory I believe).

This class had one required method, "parseChange", which accepted a string. Its job is self explanatory: it would parse said string, check for coin inputs (defined by the instructions as single capital letter strings such as "P" for penny), and return how much this translated to in dollars and cents as a float. The function is very simple, it split every single character using the list() class which generated a list that would then be looped through and compared to the accepted coin characters, incrementing the initialized coin amounts. Any leftover characters that did not matched were instead appended to a rejected_change list.

Of course, this does not actually calculate how much each of these coins represented. That's where the helper method "calculate_amount" came in. I separated the duties to reduce the responsibility of the original method. The return for "parseChange" called this new helper method. "Calculate_amount" would then create an amount float with the value of "self.penny" multiplied by .01, representing how much each penny was worth. It then went through each stored coin type, multiplied amount stored by how much it was worth and added it to the "amount" variable. I made each its own line purely for readability--I could have made it all one long line but that looks ugly. After adding the value of each stored coin to the "amount" variable, it was then passed up to "parseChange" through being returned, and then passed up once again to the actual main driver call.

========================
4. Program Flow (I.E. how "BankManager()" main function works)

When the program begins, "BankManager()" is called, beginning the main driver loop. The first thing that happens is that a "current_input" variable is initialized as None. This variable is important as it represents the input given by the user when selecting which menu option to use. A "bank" variable is also created using the "Bank()" class. This variable is important as it represents the bank being used for the entire program. Technically, this program allows for creation of multiple banks, even though this was not used for this assignment. 

The main while loop now begins. This while loop holds the logic for which banking option is being selected. It runs a simple check to ensure the user inputs an integer in range, and through comparison calls on different parts of the program to complete the connected behavior. The aforementioned mentioned classes are called along with additional global helper functions in combinations that result in the desired behavior. This allows for the "BankManager()" main function to be relatively simple; its logic is a series of checks, calls, and routing outputs rather than any direct computations. As such, it is pretty self explanatory. One of the checks, however, is more complicated.

For an input of 7, an ATM withdrawal, I found myself running into an issue when it came to one  thing: the account having a balance too low for the transaction type. This broke the usual flow as withdraw would not allow you to input 0, but the function cannot happen at multiples of 5 if you have less funds than required. So, I created a check for the account balance being under 5, and made sure to exit the function if that was the case while letting the user know what happened. Additionally, I needed a way to loop within this function for when the user would input an incorrect amount. From what I was able to understand, a check happens within withdraw, but withdraw was only called on a single if statement when I first created the function, meaning if the attempt failed the function would exit outright despite stating the withdrawal's "try again" string. To resolve this, I made a variable set to the original balance when beginning the ATM withdrawal and if your balance checked against this after being rejected had not changed, the function would loop again and re-ask you to input an acceptable number. I am aware this is a cumbersome solution but it works.

I'd like to run a quick explanation of the global functions as well.

"Draw_main" is called every time the main loop runs, and prints the program options to the screen.

"Account_list_creation" is called once, when a "Bank" object is created, and returns a list of supported accounts based on the given constant initialized as None.

"Account_creation" is called by option 1 and cycles through various calls to other functions within it to gather the necessary inputs for an "Account" class to be created.

"Account_number_creation" uses the imported random library to create an account number, verify it is not in use, and return it to the creation function.

"Get_string" is a useful function that can be adapted for its current purpose by passing in a string to that defines to the user what is being gathered, before returning the input gathered. For example, if "withdraw" is passed in, this function will replace the printed string when gathering to include withdraw as the reason: "Enter amount to {info_type} in dollars and cents(e.g. 2.57):"

"Get_ssn" is a more specialized input grabber function that ensures what you type is a social, and returns it as a string.

"Pin_creation" uses the imported random library to create a pin. This is done sequentially with each digit rather as the pin can have multiple leading 0 digits. This is converted to a string and returned.

"Change_pin" calls on "get_new_pin" to confirm a valid pin creation. It checks by comparing the user input to a second input, in order to simulate a "type again to confirm" function, updating the "account" object's pin and breaking the infinite True loop once this condition is satisfied.

"Get_pin" only confirms that a valid pin input is made, and returns it as a string.

"Get_user_account_number" confirms the user is inputting a valid account number and returns it.

"Get_amount" is similar to "get_string" but is used for getting a number representing money, and also takes a string to help define to the user what is being inputted. This function will automatically round to two digits, and does not error out if a float longer than two digits is inputted.

"Get_ssn" is similar to the other "get" functions and verifies the user input is a valid SSN, before returning it as a string.

"Get_account_multiple" once again verifies an input except in this case, it ensures the input is a multiple of 5 for use in the "CoinClass" class.

"Atm_calculation" is another helper called by the "CoinClass" class that uses logic to return an amount divided into 20, 10 and 5 dollar bills represented by aptly named variables in the most efficient order (divide into as many 20 bills as possible, followed by 10, followed by 5).

========================
5. Transactions permitted

This program allows for all required transactions to occur. This includes: Withdrawing funds, depositing funds, transferring funds between accounts, depositing funds in coin format, and withdrawing funds in bill format.


========================
6. Input validation

All instances where input is requested from the user provides some kind of input validation. These are almost always built into the helper functions rather than the main method being used. This allowed for a large amount of code reduction for what is a common but repetitive task.

========================
7. Test Cases

I tested various edge cases when creating this program. As far as I know, the finalized program is able to function with all edge cases I can think of. Of course, it is always possible one I did not come up with exists, but for candidness I want to list out some of the main of my tested cases:

1. Tested 0 for each transaction, and made sure it is never allowed
2. Tested withdrawals or transfers greater than the account balance, and made sure it was not allowed
3. Tested inputs for incorrect length and/or characters, such as letters in the SSN input, or pin strings being of the incorrect length. Each provided a feedback error to the user and allowed for another attempt except when the instructions implied no further attempts are allowed such as inputting an incorrect pin when trying to access one's account (a pin that is too short or contains non-number characters can be retried, but not one which is correctly a pin but wrong)
4. Tested the maximum accounts allowed with when the constant was set to 2, and it worked, allowing me to set it to 100 as the function did not change only the constant did.
5. Tested deletion of account, which correctly removes the "account" object from the "bank" list and effectively nullifies all information in it, while opening up a spot.
6. Tested incorrect multiple of five for ATM withdrawal, correctly rejects non-multiples, negatives and 0, and allows for new input if so
7. Tested out of range or incorrect inputs for the main driver block, program does not error out and states reason for rejected input then displays draws the menu again
8. Tested out of range or incorrect inputs for main driver block after a correct input was used in that session, caused previous correct input to persist and a selection to be made despite new input being incorrect. Fixed by setting "current_input" to None when while loop begins.
9. Tested transfers between accounts when fund transferred is too high for original account. Previous version correctly prints error but still updates balances, new version breaks the loop if amount is too high.

 
