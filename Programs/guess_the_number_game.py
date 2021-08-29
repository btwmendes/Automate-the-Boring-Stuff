# This is a guess the number game.
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,1000)
print(f'Well, {name}, I am thinking of a number between 1 and 1000.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess.

if guess == secretNumber:
    print(f'Good job, {name}! You guessed my number in {guessesTaken} tries.')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')
    diff = abs(secretNumber - guess)
    print(f'You were {diff} away from the secret number. Sorry, there is no participation trophy in this game :P')
