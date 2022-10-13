#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# password = ''  # initialize empty string
# for char in range(1, nr_letters +1):  # range from 1, to user number -1, +1to end of range
#     password += random.choice(letters)
#     # randomCharacter = random.choice(letters)  # get random item from list
#     # password += randomCharacter # put new pw in empty pw
# for char in range(1, nr_numbers +1):
#   password += random.choice(symbols)
# for char in range(1, nr_symbols +1):
#   password += random.choice(numbers)
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordList = [] #put it in list to shuffle 

for char in range(1, nr_letters +1):
    passwordList += random.choice(letters)
for char in range(1, nr_numbers +1):
  passwordList += random.choice(symbols)
for char in range(1, nr_symbols +1):
  passwordList += random.choice(numbers)

print(passwordList)
random.shuffle(passwordList)
print(passwordList)

# turn it back to a string
password = ''
for pw in passwordList:
  password += pw
print(f"Your password is: {password}")