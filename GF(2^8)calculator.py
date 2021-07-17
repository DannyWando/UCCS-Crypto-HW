'''
Daniel Wandeler
CS 4920
Homework 3 Programming problem 1

This program acts as a four-function calculator in GF(2^8). It takes in
two numbers/elements and the choice of addition, subtraction, multiplication,
or division, and performs the operations and outputs the result to the user.
'''

GF = 2 ** 8

def addGF(num1, num2):
    return print((num1 + num2) % GF)
    # do stuff

def subGF(num1, num2):
    return print((num1 - num2) % GF)
    # do more stuff

def multGF(num1, num2):
    return print((num1 * num2) % GF)
    # do even more stuff

def divGF(num1, num2):
    return print((num1 / num2) % GF)
    # do stuff again...

def calculatorGF(num1, num2, operationString):
    validInput = False
    while not validInput:
        if operationString in ['addition', 'add', 'Add', 'Addition']:
            addGF(num1, num2)
            validInput = True
        elif operationString in ['subtraction', 'sub', 'Sub', 'Subtraction']:
            subGF(num1, num2)
            validInput = True
        elif operationString in ['multiplication', 'mult', 'Mult', "Multiplication"]:
            multGF(num1, num2)
            validInput = True
        elif operationString in ['division', 'div', 'Div', 'Division']:
            divGF(num1, num2)
            validInput = True
        else:
            print('Invalid input')


doneGrading = False
while not doneGrading:
    firstNum = int(input("Enter the first number (decimal): "))
    secondNum = int(input("Enter the second number (decimal): "))
    operation = input("Which operation would you like to perform?\nAddition? Subtraction? Multiplication? Division? ")

    calculatorGF(firstNum, secondNum, operation)
    answer = input('Would you like to perform another operation? Press any key before hitting enter: ')
    if not answer:
        doneGrading = True
