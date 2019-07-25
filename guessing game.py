from random import randint
reset = True
while reset:
    low = int(input('Low number> '))
    high = int(input('Highest number> '))
    if high < low:
        print('invalid number range {}-{}'.format(low,high))
    else:
        numb = randint(low,high)
        reset = False
        guessing = True
        tries = 0
    while guessing:
        guess = int(input('Guess {}-{}> '.format(low,high)))
        tries = tries + 1
        if guess > numb:
            print('The number is lower than {}'.format(guess))
        if guess < numb:
            print('The number is higher then {}'.format(guess))
        if guess == numb:
            print('Correct, It took you {} tries to guess a number between {} and {}'.format(tries,low,high))
            if input('Play again? (y or n)> ') == 'y':
                reset = True
                guessing = False
            else:
                guessing = False
