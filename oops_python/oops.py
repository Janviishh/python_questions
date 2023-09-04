
    #methods are functions which are written inside a class oly accesible byobject of that clss.
    #function is outside class and available for everyone
# The above class represents an ATM machine with a PIN and balance attributes.
class Atm:
    #static variable always written outside the constructor
    __counter=1
    def __init__(self): #init is magic method or called constructor
        self.__pin = "" #in encapsulation we use these double  underscore to protect our data these are called dunder  __ used for private
        self.__balance = 0
        self.sno=Atm.counter
        Atm.__counter=Atm.__counter+1
        self.__menu()
    @staticmethod
    def get_counter():# we use getter and setter method in ewncapsulation for 
        return Atm.__counter
    def set_pin(new):# we use getter and setter method in ewncapsulation for 
        if type(new)==int:
            Atm.__counter=new
        else:
            print("Not allowed")

    def get_pin(self):# we use getter and setter method in ewncapsulation for 
        return self.__pin
    def set_pin(self,new_pin):
       self.__pin = new_pin
       print("pin changed")


    def menu(self):
        
        #The function displays a menu with options for creating a pin, depositing money, withdrawing
        #money, checking balance, or exiting the program.
      
        user_input = input("""
                        HELLO, HOW WOULD YOU LIKE TO PROCEED?
                        1. Enter 1 to create pin.
                        2. Enter 2 to deposit.
                        3. Enter 3 to withdraw.
                        4. Enter 4 to check balance.
                        5. Enter 5 to exit.
                        """)

       # The code block you mentioned is part of the `menu` method in the `Atm` class. It is
       # responsible for displaying a menu to the user and performing different actions based on their
       # input.
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        """
        The function `create_pin` prompts the user to enter a pin and sets it as an attribute of the
        object.
        """
        self.pin = input("Enter your pin")
        print("Pin set successfully")

    def deposit(self):
        """
        The function allows a user to deposit money into their account if they enter the correct PIN.
        """
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter amount"))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        """
        The function allows a user to withdraw a specified amount from their account if they enter the
        correct PIN and have sufficient balance.
        """
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount <= self.__balance:  # Changed < to <=
                self.__balance = self.__balance - amount
                print("Operation successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin, please check your pin")

    def check_balance(self):
        """
        The function `check_balance` prompts the user to enter a PIN and if it matches the stored PIN,
        it prints the account balance; otherwise, it prints an error message.
        """
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")

# Instantiate the ATM class
# `sbi = Atm()` is creating an instance of the `Atm` class and assigning it to the variable `sbi`.
# This allows us to access the methods and attributes of the `Atm` class through the `sbi` object.
#sbi = Atm()
# Get the counter value and print it
counter_value = Atm.get_counter()
print("Counter Value:", counter_value)
