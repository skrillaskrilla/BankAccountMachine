class BankStatement: #BankStatement class declaration
    def __init__(self): #BankStatement constructor
        _accountNumber = 0 #accountNumber for the BankStatement class (int)
        _initialBalance = 0.0 #intialBalance for the BankStatement class (float)
        _interestRate = 0.0 #interestRate for the BankStatement class (float)
        _accountHolderName = '' #accountHoldername for the BankStatement class (string)
        _monthlyDeposit = 0 #monthlyDeposit for the BankStatment class (int)
        _monthlyWithdrawal = 0 #monthlyWithdrawal for the BankStatement class (int)
    def bankProgram(self):  #bankProgram() is responsible for the input, assignment and validation of attributes the BankStatement 
        display = 'Welcome to Programming Principles Bank' #Start of bankProgram menu
        print(display) #Printing out bankProgram menu
        #Declaring inputValues for attributes
        inputAccountHolderName = '' #Initializing inputAccountHolderName variable
        inputAccountNumber = '' #Initializing inputAccountNumber variable
        inputAnnualInterestRate = '' #Intializing inputAnnualInterestRate variable
        inputInitialBalance = '' #Intializing inputInitialBalance variable
        inputMonthlyDeposit = '' #Intializing inputMonthlyDeposit variable
        inputMonthlyWithdrawal = '' #Intializing inputMonthlyWithdrawal
        bankInformationSubmitted = False #Initializing boolean for while loop information
        splitName = '' #Initializing splitName as an empty string to be split later for the inputBankHolderName
        Name = '' #Concatenating firstName and lastName if lastName exists
        try:
            while(bankInformationSubmitted != True): #Ask user all of information until the user reaches to the end
                #Input, Assignment, Validation for the _accountHolderName
                while(Name.isalpha() != True ): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
                    try:
                        inputAccountHolderName = input('Please enter the name of the account holder: ') #Input
                        if inputAccountHolderName.isdigit(): #Validation
                            print('Please enter a valid name')
                            continue   
                        splitName = inputAccountHolderName.split() #Split the inputAccountHolderName
                        firstName = splitName[0] #Assign the firstName to the 0 index of the splitName list
                        Name = firstName #Name is equal to the firstName
                        if(len(splitName) == 1):
                            self._accountHolderName = Name
                        if(len(splitName) == 2): #Yet, if the length of it is 0-1 then it is going to be a lastName 
                            lastName = splitName[1] #Assign the lastName to the splitName 2nd index
                            Name += lastName.capitalize() #Concatanate this name to the Name as a condition to get out of the while loop
                            self._accountHolderName = firstName + ' ' + lastName #Assignment of _accountHolderName and readd the white space that was removed after the split of the inputAccountHolderName
                    except ValueError: #If there are any ValueErrors be able to handle it
                        print('Please enter a valid name')
                #Input, Assignment, Validation for the _accountNumber
                while(inputAccountNumber.isdigit() != True or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000): #While loop until inputAccountNumber.isDigit() is not equal to True or until inputAccount Number is less than 100 and until Greater than 1000
                    try:
                        inputAccountNumber = input('Please enter the account number [100 - 1000]: ') #Input
                        if inputAccountNumber.isalpha() or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000 : #Validation
                            print('Please enter a valid account number')
                            continue
                    except ValueError:
                        print('Please enter a valid account number')
                self._accountNumber = inputAccountNumber  #Assignment of _accountNumber
                #Input, Assignment, Validation for the _accountAnnualInterestRate
                while(type(inputAnnualInterestRate) != float): #While the inputOfAnnualInterest is a float
                    inputAnnualInterestRate = input('Please enter the annual interest rate percentage [> 0]: ')
                    if inputAnnualInterestRate.isalpha() or float(inputAnnualInterestRate) < 1: #Validate that inputAnnualInterestRate is not alphabetical and less than 100
                        print('Please enter a valid annual interest rate.')
                    float(inputAnnualInterestRate) #Converting inputAnnualInterestRate from string to int
                    if inputAnnualInterestRate.isdigit(): #If inputAnnualInterestRate is a digit then,
                        inputAnnualInterestRate = int(inputAnnualInterestRate) / 100 #Turn the whole number into a percentage by dividing the inputAnnualInterestRate by 100
                        float(inputAnnualInterestRate) #Convert inputAnnualInterestRate into a float
                self._interestRate = inputAnnualInterestRate #Assignment of _interestRate to the inputAnnualInterestRate of the user 
                #Input, Assignment, Validation for the _initialBalance
                while(type(inputInitialBalance) != float): # While loop until the inputInitialBalance is equal to a float
                    inputInitialBalance = input('Please enter the initial balance [>= 0]: ')
                    if inputInitialBalance.isalpha() == True:#Validate that inputIntialBalance is not alphabetical
                        print('Please enter a valid balance that is numeric.')
                    inputInitialBalance = float(inputInitialBalance)     
                    if inputInitialBalance <= 0:  #Validate that inputInitialBalance less than or equal to 0
                        print('Please enter a valid balance greater than 0.')
                self._initialBalance = inputInitialBalance
                #Input, Assignment, Validation for the _inputMonthlyDeposit  
                while(type(inputMonthlyDeposit) != float): # While loop until the inputInitialBalance is equal to a float
                    inputMonthlyDeposit = input('Please enter the monthly deposit [> 100]: ')
                    if inputMonthlyDeposit.isalpha() == True:#Validate that inputIntialBalance is not alphabetical
                        print('Please enter a valid balance that is numeric.')  
                    if float(inputMonthlyDeposit) < 100:  #Validate that inputInitialBalance less than or equal to 0
                        print('Please enter a valid balance greater than 100.')
                    if float(inputMonthlyDeposit) >= 100:
                        inputMonthlyDeposit = float(inputMonthlyDeposit) 
                self._MonthlyDeposit = inputMonthlyDeposit 
                #Input, Assignment, Validation for the _inputMonthlyWithdrawal 
                while(type(inputMonthlyWithdrawal) != float): # While loop until the inputMonthlyWithdrawal is equal to a float
                    inputMonthlyWithdrawal = input('Please enter the monthly withdrawal [< 1000]: ')
                    if inputMonthlyWithdrawal.isalpha() == True:#Validate that inputMonthlyWithdrawal is not alphabetical
                        print('Please enter a valid balance that is numeric.')  
                    if float(inputMonthlyWithdrawal) < 1000:  #Validate that inputMonthlyWithdrawal less than or equal to 0
                        print('Please enter a valid balance greater than 1000.')
                    if float(inputMonthlyWithdrawal) >= 1000:
                        inputMonthlyWithdrawal = float(inputMonthlyWithdrawal) 
                self._monthlyWithdrawal = inputMonthlyWithdrawal  
                bankInformationSubmitted = True
        except:
            print('Something wrong has happened here...')
    
    #This method will be responsible for the print of the _bankAccountNumber, _accountHolderName,
    #def displayBankStatement ():
    