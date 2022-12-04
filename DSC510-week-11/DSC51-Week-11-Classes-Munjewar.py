import locale
# ------------------------------------------------------------------------#
# Title         : Week-11-Classes.
# Author        : Sheetal Munjewar
# University    : College of Science and Technology, Bellevue University
# Course        : DSC 510 T302 Introduction to Data Science (2227-1)
# Professor     : Michael Eller
# Initial Draft : 11/13/2022
#-------------------------------------------------------------------------#


#--Pretty Print function wiht one input parmater, no return value.
def func_print():

    locale.setlocale(locale.LC_ALL, '')
    print("{:->50}".format(""))
    print("Report Summary".center(50, " "))
    print("{:->50}".format(""))
    print("{:>20} {}".format("Item Count:",register.get_count()))
    print("{:>20} {}".format("Total Price:",register.get_total()))
    print("{:->50}".format(""))

class CashRegister:

    def __init__(self):
        self.total = 0.0
        self.count = 0

    def add_items(self, price):
        self.total += price
        # self.total = self.total + price
        self.count += 1

    def get_total(self):
        return locale.currency(self.total, grouping=True)

    def get_count(self):
        return self.count

    def clear_cart(self):
        self.total = 0.0
        self.count = 0

def main():

    '''Your program must have a header.
    Your program must have a welcome message for the user.
    Your program must have one class called CashRegister.
    Your program will have an instance method called addItem which takes one
    parameter for price. The method should also keep track of the number of
    items in your cart.
    Your program should have two getter methods.
    getTotal – returns totalPrice
    getCount – returns the itemCount of the cart
    Your program must have a properly defined main function and a call to main.
    Your program must create an instance of the CashRegister class within your
    main function.
    Your program should have a loop in main which allows the user to continue
    to add items to the cart until they request to quit.
    Your program should print the total number of items in the cart.
    Your program should print the total $ amount of the cart.
    The output should be formatted as currency. Be sure to investigate the
    locale class. You will need to call locale.setlocale and locale.currency.
    Your program should adhere to PEP8 guidelines especially as it pertains
    to variable names.
    '''


print("Welcome to CashRegister :")
while True:
    usr_input = input("\nPress 'y' to cont. and 'q' to quit(): ")
    # print(len(usr_input))
    # print(usr_input.lower())
    if usr_input.lower() == 'q':
        register.clear_cart()
        print("Thanks for visiting !")
        break
    elif len(usr_input) == 0 or usr_input.strip().lower() != 'y':
        print ("Invalid Input : {}, Please try again".format(usr_input))
    else:
        register = CashRegister()
        try:
            item_cnt = int(input("How many item you would like to insert: "))
        except ValueError as e:
            print("Invalid Input: {}".format(e))
            continue

        for i in range(item_cnt):
            try:
                item_price = float(input("Insert item price: "))
            except ValueError as e:
                print("Invalid Input: {}".format(e))
                continue
            else:
                register.add_items(item_price)

        #-- Calling function to print to the report.
        func_print()
        # print(f"Item count : {register.get_count()}")
        # print(f"Total price : {register.get_total()}")

if __name__ == "__main__": main()
