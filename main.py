import random


print('Welcome to Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

lenght = input('Input your password lenght: ')
lenght = int(lenght)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
    