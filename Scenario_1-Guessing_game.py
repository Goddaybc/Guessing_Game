#import random module
import random
#generate random number
my_number = random.randrange(1, 10)
#initialize variables
my_guess = 0
guess_count = 0
#use a loops to check the various conditions
while my_guess!= my_number and my_guess != "exit":
    my_guess = input("Please enter number from 1 to 10: ")
    if my_guess == "exit":
        print ("Game Over")
        break
    my_guess = int(my_guess)
    guess_count += 1
    if my_guess == my_number:
        print ("\nCongratulations you guess it")
    elif my_guess > 10 or my_guess < 0:
        print("Your guess is out of range")
    elif my_guess > my_number:
        print ("Lower number please")
    elif my_guess < my_number:
        print("Higher number please")
else:
    print(f"\nYou got it at {guess_count} attempts")
