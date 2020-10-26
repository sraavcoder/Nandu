a = input("Enter Any Word ___ ")
import random

print(random.randint(0, 13))

number = 1

for i in a:
    if(i == ' '):
        number = number + 1

print(f'The No.of Characters in your Word is {number} ')
