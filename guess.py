import random
def guess(x):
    rand_num=random.randint(1,x)
    guess=0;
    while guess!=rand_num:
        guess=int(input(f"Guess the number from 1 to{x}:"))
        if guess<rand_num:
            print("Sorry!Guess again.It is too Low")
        elif guess>rand_num:
            print("Sorry!Guess again .It is too High")

    print( f"Yay!you guessed the number {rand_num} correctly!!")

guess(100)
            
