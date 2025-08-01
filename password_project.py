import random
import string
print("Welcome to the Password Generator!")
# question about the lenght of the password
total_characters=int(input("Enter the total number of characters in the password: "))
total_number=[]
# ask the user about the  lenght of the numbers and letters and symbols in the password and append each one to the total_number list 
if total_characters>0:
  letters_number=int(input("Enter the number of letters in the password: "))
  if letters_number>=0:
    total_number.append(letters_number)
  numbers_number=int(input("Enter the number of numbers in the password: "))
  if numbers_number>=0:
    total_number.append(numbers_number)
  symbols_number=int(input("Enter the number of symbols in the password: "))
  if symbols_number>=0:
    total_number.append(symbols_number)
    # check if the sum of the numbers is equal to the total number of characters
  if sum(total_number)==total_characters:
    random_letters=random.choices(string.ascii_letters,k=letters_number)
    random_numbers=random.choices(string.digits,k=numbers_number)
    random_symbols=random.choices(string.punctuation,k=symbols_number)
    password=random_letters+random_numbers+random_symbols
    random.shuffle(password)
    random_password="".join(password)
    print("Generated password: ",random_password)
  else:     
    print("Invalid input. The sum of the letters, numbers, and symbols dosn't match the password length.")
else:
  print("Invalid input. Please try again and enter a positive number.")

