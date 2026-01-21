import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['@','#','$','&','!']
number_of_letters = input('How many alphabet do you needed to added to you password?\n')
number_of_numbers = input('How many number are you planning to add to your password?\n')
number_of_symbol = input('How many symbol are you planning to add to your password?\n')

password = ''

for char in range(1, int(number_of_letters) + 1):
    random_char = random.choice(alphabet)
    password += random_char
for number in range(1, int(number_of_numbers) + 1):
    random_num = random.choice(numbers)
    password += random_num
for symbol in range(1, int(number_of_symbol) + 1):
    random_sym = random.choice(symbols)
    password += random_sym
random_password = random.sample(password, len(password))
password = ''.join(random_password)
print(password)

random_alpha = random.sample(alphabet, int(number_of_letters))
random_num = random.sample(numbers, int(number_of_numbers))
random_sym = random.sample(symbols, int(number_of_symbol))
serial_password = random_alpha + random_num + random_sym
random_password =''.join(random.sample(serial_password, len(serial_password)))
print(random_password)
