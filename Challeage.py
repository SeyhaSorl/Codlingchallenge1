import random
num = random.randint(1,10)



while True :
    guess = int(input("guess the number (1-10):"))
    if (guess > num ):
        print ( "The number is lower than (guess)🤔🤔🤔 "  )
    elif (guess < num):
        print("the number is highder than (guess)😒")
    else:
        print (f"Cong you got the correct number :(❁´◡`❁){num}")
        break