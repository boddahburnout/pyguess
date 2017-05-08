from random import randint
found = False
tries = 0
lowval = int(input("Lowest value: "))
highval = int(input("Highest value: "))
answer = randint(lowval, highval)
while not found:
    print ("Guess a number "+ str(lowval) +"-"+ str(highval))
    guess = int(input("Guess: "))
    tries = tries + 1
    if guess == answer:
        print ("Correct")
        print ("Tries: "+ str(tries))
        again = input("Play Again?: ")
        if again == "yes":
            lowval = int(input("Lowest value: "))
            highval = int(input("Highest value: "))
            answer = randint(lowval, highval)
            guess = 0
            tries = 0
            found = False
        if again != "yes":
                print ("See ya!")
                found = True
        if guess > highval:
            print (str(guess)+" is greater then "+ str(highval)+" Duh")
    else:
        print ("Wrong")
            
