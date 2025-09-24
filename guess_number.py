import random
# Generate random number between 1 and 50
secrete_number = random.randint(1, 50)

attempts = 0
guess = 0
print("Welcome to the guess-the-Number Game!")
print("I have choosen a number between 1 and 50, Can you guess it?")

while guess != secrete_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
       
        if guess < secret_number:
             print("Too slow! Try again.")   
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secrete_number}.")
            print(f"you guesed it in {attempts} attempts.")
   
    except ValueError:
         print("Please enter a valid number,")
