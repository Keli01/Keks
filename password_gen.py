#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

data_valid = False
while data_valid == False:

  #Accept password length from user.
  
    nr_characters = input("Enter your desired password length\n")
    try:
      nr_characters = int(nr_characters)
    except:
      print("Error! Password length should be a number.")
      continue
    if nr_characters < 6:
      print("Password length cannot be less than 6 characters.")
      continue
    else:
      data_valid = True
        
data_valid = False
while data_valid == False:
  nr_letters = input("How many letters would you like in your password?\n")
  try:
    nr_letters = int(nr_letters)
  except:
    print('Error! Only numbers are accepted.')
    continue
  if nr_letters <= 0:
    print('Error! Enter a number greater than zero. ')
    continue
  else:
    data_valid = True

data_valid = False
while data_valid == False:
  nr_symbols = input(f"How many symbols would you like?\n")
  try:
    nr_symbols = int(nr_symbols)
  except:
    print('Error! only numbers are accepted.')
    continue
  if nr_symbols <= 0:
    print('Error! This field cannot be less than or equal to zero.')
    continue
  else:
    data_valid = True

data_valid = False
while data_valid == False:
  nr_numbers = input(f"How many numbers would you like?\n")
  try:
    nr_numbers = int(nr_numbers)
  except:
    print('Error! Only numbers are accepted.')
    continue
  if nr_numbers <= 0:
    print('Error! This field cannot be less than or equal to zero.')
    continue
  else:
    data_valid = True

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

for char in range(1, nr_letters + 1):
  random_char = random.choice(letters)
  password += random_char
for sym in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym
for num in range(1, nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num
pass_word = "".join(random.sample(password, len(password)))
print('Your password is',pass_word)