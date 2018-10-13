# BankAccountMVC
This is Team Tral's Final Project for ACIT 2515 Term 2 April 2018 2A

Team Tral's Members:
Alex Phan A01019714
Travis Chan A01024065
----------------------------------------------------------------
TABLE OF CONTENT:
----------------------------------------------------------------

*WHO DID WHAT?* - 17
*INTRODUCTION* - 45
*IMPORTANT(How to Run Program)* - 53
*HOW TO USE* - 67

----------------------------------------------------------------
*WHO DID WHAT?*
----------------------------------------------------------------
Alex Phan 
- Writing/Reading into .csv
- Writing/Reading into .txt
- ATM GUI Transaction Log
- ATM GUI View (Half)
- ATM GUI Controller (Half)
- ATM GUI Model
- Bank CLI Withdraw
- Bank CLI Deposit
- Bank CLI Balance
- Bank CLI Chequing/Saving
- Refactor to MVC

Travis Chan
- ATM GUI Login
- ATM GUI View (Half)
- ATM GUI Controller (Half)
- Bank CLI Login
- Bank CLI Model
- Bank CLI Controller
- Bank CLI View
- Refactor From Hard Code to Soft Code
- Changing Windows Back and Forth
- Having buttons disappear and re-appear based on the type of account (Chequing, Saving, or Both)

----------------------------------------------------------------
*INTRODUCTION*
----------------------------------------------------------------

In the zip Final MVCBankAccount folder, the ATM GUI and Bank Teller CLI works together. For example, if you create an account from the Bank Teller CLI, you can login with that account in ATM GUI. Both, ATM GUI and Bank Teller CLI zip dist folder DO NOT WORK TOGETHER, because the ATM GUI and Bank Teller CLI are both using a different csv file. They run separately.

This program is separated into 3 folder for model, view, control.

----------------------------------------------------------------
*IMPORTANT*
----------------------------------------------------------------

To run the ATM GUI:
Run ATM.py
ATM Account# = 925184
ATM Pin = 111111

To run the Bank Teller CLI:
Run Bank_Teller_CLI.py
Bank Teller Account# = 123
Bank Teller Password = 123

---------------------------------------------------------------
*HOW TO USE*
---------------------------------------------------------------

In ATM GUI, you sign in with ATM Account# and ATM Pin. Then, click the buttons all the way through.

In Bank Teller CLI, you can Manage Accounts,for example withdraw, deposit and check balances from accounts, and Create Account. To use the CLI, type the number of the command. For example, if you want to Manage Account, type "1" after ">>>".

--Account Management--
 1. Manage Account
 2. Create Account
 3. Sign Out
>>> 1



