import re
import random
import string
    
# check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Too short and it is weak atleast contains min 8 letter)"
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    passed = length + bool(upper) + bool(lower) + bool(digit) + bool(symbol)

    if passed == 5:
        return "Very Strong "
    elif passed >= 3:
        return "Medium "
    else:
        return "Weak"

# generate strong password
def generate_password(length):
    if length < 8:
        return "Length must be at least 8 characters."

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = upper + lower + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

#Menu
print("Welcome to Smart Password Tool 🔐")

while True:
    print("\nMenu:")
    print("1 → Generate Password")
    print("2 → Check Password Strength")
    print("3 → Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        length = int(input("Enter password length (min 8): "))
        pwd = generate_password(length)
        print("Generated Password:", pwd)
        print("Strength:", check_password_strength(pwd))

    elif choice == '2':
        user_pwd = input("Enter your password: ")
        result = check_password_strength(user_pwd)
        print("Password Strength:", result)

    elif choice == '3':
        print("Goodbye Akshay! ")
        break

    else:
        print("Please enter 1, 2, or 3 only.")

