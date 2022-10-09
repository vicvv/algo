'''
ask user a to enter start and end number, make sure they are int, generate random num
and ask to guess. return the number of tries it took to guess a number
'''


import random

s = input("Enter the start of the range: ")
while not s.isdigit():
    print('Please enter a valid number.')
    s = input("Enter the start of the range: ")
  
e = input("Enter the end of the range: ")  
while not e.isdigit() or int(e) < int(s):
    print('Please enter a valid number.')
    e = input("Enter the end of the range: ")

num = random.randint(int(s), int(e))
att = 0
guess = None


while guess != str(num):
    guess_num = input("Guess a number: ")
    if not guess_num.isdigit():
        print('Please enter a valid number.')
        continue
    guess = guess_num
    att +=1

suff ='' if att==1 else 's'
print('You guessed the number in ' + str(att) + ' attempt'+suff)