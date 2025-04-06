import random
playing = True
number = str(random.randint (10,20))
print("I will give a number from 0 - 9 you have to guess the number one digit at a time.")
print("The game ends when you guess 1 correct.")
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("Woo Hoo, You guessed it right!!")
        print("The number was", number)
        break
    else:
        print("Ohh Your guess was wrong!!, not to worry you can try again. \n")