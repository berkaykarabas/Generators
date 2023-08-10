#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = [letters, numbers, symbols]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
my_password = []

for i in range(0,nr_letters):
    my_choose_letter =random.choice(letters)
    my_password.append(my_choose_letter)
for j in range(0,nr_symbols):
    my_choose_symbols =random.choice(symbols)
    my_password.append(my_choose_symbols)
for k in range(0,nr_numbers):
    my_choose_numbers =random.choice(numbers)
    my_password.append(my_choose_numbers)
my_letter = ""
for i in range(0,len(my_password)):
    my_letter += random.choice(my_password)
print(my_letter)
