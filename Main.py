
from random import randint
from pip._vendor.distlib.compat import raw_input
checker = True
print("Name of the game is dice kid try to get a 6 good luck")
number = (randint(1, 6))
checker = True

while checker:
    print (number)
    
    if number == 6:
        print("Nice one")#
        checker = False
    
    else:
        second_guess = raw_input("unlucky would you like to roll again yes or no?")
        if second_guess == "yes":
            number = (randint(1, 6))
        
        else:
            checker = False
        

    





 



