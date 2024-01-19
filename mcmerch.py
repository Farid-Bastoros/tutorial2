# MVP Plan
# 1. Get enviroment set up 
#  - one by one istead of many items
#  - one province instead of many (ON)
#  - Calculate tax + 5% discount for ON item  


ON_TAX = 0.13
DISCOUNT = 0.05

def main():
    item_price = float(input("Enter the price of the item:"))

    price_after_discount = item_price * (1 -DISCOUNT)
    item_tax = price_after_discount * ON_TAX

    final_price = price_after_discount + item_tax

    print("Final price for the item is ${:.2f}".format(final_price))



"""
# Tutorial 2 Python File # mcmerch.py

import sys

def parseArguments():
    arguments = { 
        "price": int(sys.argv[1]),
        "quantity" : 1 , 
        "province" : "ON"
    }
    
    return arguments


def taxRate():
    tax = {
        "ON" : 0.13
        
    }
    return tax[province]

def mcmerchCalculator ():
    arguments = parseArguments()
    tax = taxRate(arguments['province'])
    print(arguments['price'] * arguments['quantity'] * (1 +tax))

mcmerchCalculator()
    


"""