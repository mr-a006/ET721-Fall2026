"""
Aqeel Hussain
Oct 5, 2026
lab 9: unit testing using Pytest
"""
# exercise
def multiply(a,b):
    return a*b

def divide (a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a/b

# exercise 2
# create a function that validates a password: 8+ characters, contains at least one digit
def validate_password(password):
    if len(password) < 8:
        return False
    return any(char.isdigit() for char in password)

# exercise 3
# create a function that checks if a number is even