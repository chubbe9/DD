import random

guesses_made = 0

name = input('TEST\n')

number = random.randint(1, 20)
print ('TEST, {0}.'.format(name))

while guesses_made < 6:

    guess = int(input('Test '))

    guesses_made += 1

    if guess < number:
        print ('TEST LOW')

    if guess > number:
        print ('TEST High.')

    if guess == number:
        break

if guess == number:
    print ('TEST, {0}TEST  {1}'.format(name, guesses_made))
else:
    print ('TEST {0}'.format(number))
