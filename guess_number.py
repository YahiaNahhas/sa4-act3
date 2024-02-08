number = '10' 
cap = 4
print("I'm thinking of a number...")

guess = str(input("What number am I thinking of? "))
 
while guess != number and guess != 'q' and cap != 0:
    print("Incorret guess. Try Again!")    
    print(f"You have {cap} Number of Guesses left!")
    guess = str(input("What number am I thinking of? "))
    cap = cap-1


if guess == number:
     print("Congratulations! you guessed the right number. ")
elif guess == 'q':
     print(f"Sorry! the number was {number}.")
elif cap == 0:
     print(f"you ran out of Guesses! \n The number was {number}, Better luck next time!")
    