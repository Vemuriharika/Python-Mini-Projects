import random
import string
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*"
print("welcome to the pypassword generator")
l_count= int(input("how many letters would you like in your password?"))
s_count = int(input("How many symbols would you like?"))
n_count = int(input("How many numbers would you like?"))
password_list = []
for i in range(l_count):
    password_list.append(random.choice(letters))
for i in range(s_count):
    password_list.append(random.choice(symbols))
for i in range(n_count):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ''.join(password_list)
print(password)