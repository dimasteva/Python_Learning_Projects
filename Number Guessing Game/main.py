import random

def GuessNumber():
    target = random.randint(1, 100)
    print("How many times do you want to guess?")
    n = int(input())
    for i in range(n):
        print("Enter your guess (1 - 100): ")
        while True:
            try:
                num = int(input())
                if 1 <= num <= 100:
                    break
                else:
                    print("Out of bounds, enter the number again: ")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 100.")
        
        if num == target:
            print("Good job")
            return
        elif (i == n - 1):
            print("You did not guess the number was", target)
            return
        elif num > target:
            print("Lower")
        else:
            print("Higher")

def PlayAgain():
    while True:
        print("Do you want to play again (YES/NO)")
        ans = input().strip().upper()
        if ans == "YES":
            return True
        elif ans == "NO":
            return False
        else:
            print("Please enter YES or NO")

while True:
    GuessNumber()
    if not PlayAgain():
        break
