number = '10' 

print("I'm thinking of a number...")

guess = str(input("What number am I thinking of? "))
 
while guess != number and guess != 'q':
    print("Incorret guess. Try Again!")    

    guess = str(input("What number am I thinking of? "))

if guess == number:
     print("Congratulations! you guessed the right number. ")
elif guess == 'q':
     print(f"Sorry! the number was {number}.")
  
    