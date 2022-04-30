import random
chances = 0
n = random.randint(1,9)

while chances < 5:
    guess = int(input('Enter A Number (Range of 1 to 9): '))

    if guess > n:
        input('Too High! Guess a lower number')
        chances += 1
        # print("You have", chances + " chances left")
    elif guess < n:
        input('Too Low! Guess a higher number')
        chances += 1
        # print("You have", chances + " chances left")
    else:
        print('Congrats! You got it in', chances + 1)
        break

if not chances < 5:
    print("GAME OVER! The number was", n)