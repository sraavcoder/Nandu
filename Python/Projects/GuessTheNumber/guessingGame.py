import random

number = random.randint(1, 9)

limit = 0

while(limit < 5):
    try:
        userAnswer = int(input("Guess A Number From 1 to 9 : "))
        if(userAnswer > 9 or userAnswer < 1):
            print("Pls Give Correct Input")
    except:
        print("Pls Give Correct Input")

    if(userAnswer == number):
        print("Congratulations!! Your Guess Is Correct")
        limit = 6
    elif (userAnswer > number):
        print("Your Guess is Bigger than My number")
    elif (userAnswer < number):
        print("Your Guess is Smaller than My number")

    limit = limit + 1

if(limit == 5):
    print("Your Chances Are Completed")
    print(f'My Number Is {number} ')
