'''
Created on 30 nov. 2015

@author: Vlad Cincean
'''
from utils.utils import check_representation
from domain.operations import add, sub, mul, div
from domain.conversions import substitution_method, successive_divisions_method
from domain.rapid_conversions import rapid_convert
 
def main_menu():
    do_exit = False
    while not do_exit:
        menu = "Please select an option: \n"
        menu += "1. Perform an elementary OPERATION \n"
        menu += '2. Perform a CONVERSION \n'
        menu += '3. Perform a RAPID CONVERSION \n'
        menu += "0. EXIT \n"
        print(menu)
        cmd = str(input("Enter command: ")).strip()
        if cmd == '0':
            do_exit = True
        elif cmd == '1':
            perform_operation()
        elif cmd == '2':
            perform_conversion()
        elif cmd == '3':
            perform_rapid_conversion()
        else:
            print("Wrong command!")
            
def perform_operation():
    welcome_msg = "Hello! Here you can perform one of the four elementary operations:\n"
    welcome_msg += "+ (addition of two integer numbers in base p)\n"
    welcome_msg += "- (subtraction of two integer numbers in base p)\n"
    welcome_msg += "* (multiplication of a integer number in base p by a digit in base p)\n"
    welcome_msg += "/ (division of a integer number in base p by a digit in base p)\n\n"
    welcome_msg += "First of all, please enter the base 'p' in which you want the computations to be made :) \n"
    welcome_msg += "It can be 2, 3, 4, ..., 9, 10 or 16 \n"
    print(welcome_msg)
    p = str(input("The base p = ")).strip()
    try:
        p = int(p)
        if p >= 2 and p <= 10 or p == 16:
            print("You choosed to work in base " + str(p) + ".")
            msg = "Now, please enter the full expression of the operation you want to perform. \n"
            msg += "Use adequate operators (+, -, * or /) to do so. \n"
            msg += "P.S. Please, do not use white-spaces in the expression :) \n"
            msg += "For example, if you want to add '1' to '101', enter '1+101' (without quotation marks) \n"
            print(msg)
            executa = True
            while executa:
                expr = str(input("Expression: ")).strip()
                if '+' not in expr and '-' not in expr and '*' not in expr and '/' not in expr:
                    print("Wrong expression!")
                elif '+' in expr:
                    t = expr.upper().split("+")
                    if len(t) != 2:
                        print("Wrong expression! The operation is binary!")
                    elif check_representation(t[0], p) == False or check_representation(t[1], p) == False:
                        print("Wrong expression! Invalid number representation!")
                    else:
                        print(t[0] + " + " + t[1] + " = " + add(t[0], t[1], p))
                elif '-' in expr:
                    t = expr.upper().split("-")
                    if len(t) != 2:
                        print("Wrong expression! The operation is binary!")
                    elif check_representation(t[0], p) == False or check_representation(t[1], p) == False:
                        print("Wrong expression! Invalid number representation!")
                    elif p < 10 and int(substitution_method(t[0], p, 10)) < int(substitution_method(t[1], p, 10)):
                        print("Wrong expression! The subtrahend cannot be greater than the minuend!")
                    elif p > 10 and int(successive_divisions_method(t[0], p, 10)) < int(successive_divisions_method(t[1], p, 10)):
                        print("Wrong expression! The subtrahend cannot be greater than the minuend!")
                    elif p == 0 and int(t[0]) < int(t[1]):
                        print("Wrong expression! The subtrahend cannot be greater than the minuend!")
                    else:
                        print(t[0] + " - " + t[1] + " = " + sub(t[0], t[1], p))
                elif '*' in expr:
                    t = expr.upper().split("*")
                    if len(t) != 2:
                        print("Wrong expression! The operation is binary!")
                    elif check_representation(t[0], p) == False or check_representation(t[1], p) == False:
                        print("Wrong expression! Invalid number representation!")
                    elif len(t[1]) != 1:
                        print("Wrong expression! Can only perform multiplication by one digit!")
                    else:
                        print(t[0] + " * " + t[1] + " = " + mul(t[0], t[1], p))
                elif '/' in expr:
                    t = expr.upper().split("/")
                    if len(t) != 2:
                        print("Wrong expression! The operation is binary!")
                    elif check_representation(t[0], p) == False or check_representation(t[1], p) == False:
                        print("Wrong expression! Invalid number representation!")
                    elif len(t[1]) != 1:
                        print("Wrong expression! Can only perform division by one digit!")
                    else:
                        try:
                            q, r = div(t[0], t[1], p)
                            print(t[0] + " / " + t[1] + " = " + str(q) + " remainder " + str(r))
                        except ValueError as err:
                            print(err)
                while True:
                    a = input("Do you want to perform another operation in base " + str(p) + "? (Y/N)").lower().strip()
                    if a == 'y' or a == 'yes' or a == 'da':
                        break
                    elif a == 'n' or a == 'no' or a =='nu':
                        executa = False
                        break
                    else:
                        print("Wrong command!")
        else:
            print("Error! Cannot perform operations in the given base.")
    except ValueError:
        print("Warning! A base is always represented as a decimal integer number!")
        
def perform_conversion():
    welcome_msg = "Hello! Here you can perform a conversion.\n\n"
    welcome_msg += "First of all, please enter the source base 's' and the destination base 'n' :) \n"
    welcome_msg += "These can be 2, 3, 4, ..., 9, 10 or 16 \n"
    print(welcome_msg)
    try:
        s = int(input("The source base = "))
        d = int(input("The destination base = "))
        print("Great! Now, please enter the number's representation in base "+str(s)+" you want to convert into base "+str(d)+".")
        n = str(input("n = ")).upper()
        if check_representation(n, s) == False:
            print("Error! Invalid number representation in base "+str(s)+".")
        else:
            try:
                if s < d:
                    res = substitution_method(n, s, d)
                    print(n+" in base "+str(s)+" = "+res+" in base "+str(d))
                    print("Note: this conversion was performed using the SUBSTITUTION method.")
                elif s > d:
                    res = successive_divisions_method(n, s, d)
                    print(n+" in base "+str(s)+" = "+res+" in base "+str(d))
                    print("Note: this conversion was performed using the SUCCESSIVE DIVISIONS method.")
                elif s == d:
                    print(n+" in base "+str(s)+" = "+n+" in base "+str(d)+", obviously :)")
            except ValueError as ms:
                print(ms)
    except ValueError:
        print("Warning! A base is always represented as an decimal integer number!")
            
def perform_rapid_conversion():
    try:
        executa = True
        while executa:
            s = 0
            while s != 2 and s != 4 and s != 8 and s != 16:
                s = int(input("Source base (2, 4, 8 or 16): "))
            n = str(input("The number to convert from base "+str(s)+": ")).upper().strip()
            if check_representation(n, s) == False:
                print("Invalid number representation in base "+str(s)+"!")
                a = input("Try again (Y/N)? ").lower().strip()
                if a != 'y' and a != 'yes' and a != 'da':
                    executa = False
            else:
                d = 0
                while d != 2 and d != 4 and d != 8 and d != 16:
                    d = int(input("Destination base (2, 4, 8 or 16): "))
                if s == d:
                    print(n+" in base "+str(s)+" = "+n+" in base "+str(d)+", obviously!")
                else:
                    res = rapid_convert(n, s, d)
                    print(n+" in base "+str(s)+" = "+res+" in base "+str(d))
                a = input("Another one (Y/N)? ").lower().strip()
                if a != 'y' and a != 'yes' and a != 'da':
                    executa = False
    except ValueError:
        print("Warning! A base is always represented as an decimal integer number!")
        