
from random import randint
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
        print("unlucky lets roll again")
        number = (randint(1, 6))
        

    





 



