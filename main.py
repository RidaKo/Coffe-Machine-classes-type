from time import sleep
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
Menu = Menu()
MoneyMachine = MoneyMachine()
CoffeeMaker = CoffeeMaker()

def Reset():
    sleep(3.5)
    os.system("clear")
    Main()

def Main():
    choice = input("What kind of drink would you like? ")
    if choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
        Reset()
    else:
        drink = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(drink):
            if MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)
                Reset()
            else:
                Reset()
        else: 
            print("The resources are insufficient.")
            Reset()
os.system("clear")
Main()