number = 10 

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! you guessed the right number. ")
else:
    print(f"Sorry! the number was {number}.")