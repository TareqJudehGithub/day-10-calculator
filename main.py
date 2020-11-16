from art import logo
from replit import clear



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

def calculator():
  print(logo)
  print('''
  ''')

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }
  
  num1 = float(input("Enter a number: "))
  
  cancel = False
  while cancel == False:
    operation_symbol = input("Pick an operator (+, -, *, or /): ")
    num2 = float(input("Enter a number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    print("")
    more_trans = input("'y' continue, 'c' new transaction, or 'q' to quit: ").lower()
    if more_trans == "y":
      num1 = answer
    elif more_trans == "c":
      cancel = True
      clear()
      
      calculator()
    else:
      print("")
      print("Good Bye!")
      break

 
calculator()