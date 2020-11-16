from art import logo
from math import ceil

print(logo)
print('''
''')

# Calculator

# Add
def add(n1, n2):
  return n1 + n2


# Subtract
def subtract(n1, n2):
  return n1 - n2


# Multiply
def multiply(n1, n2):
  return n1 * n2


# Divide
def divide(n1, n2):
  if n2 == 0:
    return "nan"
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("Enter the first number: "))
operation_symbol = input("Pick an operator (+, -, *, or /): ")
num2 = int(input("Enter the second number: "))

calculation_function = operations[operation_symbol]
answer =  round(calculation_function(num1, num2), 3) 

print(f"{num1} {operation_symbol} {num2} = {answer}")