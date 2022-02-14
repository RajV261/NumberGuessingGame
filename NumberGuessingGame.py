import random

score=1

while True:
    n=int(input("Enter Any Two Digit Number : "))

    x = random.randint(10, 100)

    if (n == x):
        print("You Guessed The Correct Number")
        break

    else:
        print("Please Try Again")
        score += 1
print("It took you" ,score, "guesses")
