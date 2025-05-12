import random
number_to_guess=random.randint(1,200)
while True:
    try:
        guess= int(input("Guess the number between 1 and 100:  "))
        if guess>number_to_guess:
            print("Too high!")
        elif guess<number_to_guess:
            print("To Low!")
        else:
            print("Congratulations you guessed it true!")
    except ValueError:
        print('Please enter a valid number')
