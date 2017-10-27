#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


start_number = input("please enter a number")
start_number = int(start_number)

if((start_number % 2 == 0) and (start_number % 4 ==0)):
	print("Congrats " + str(start_number) + " is an even number and a multiple of 4")

elif((start_number % 2 == 0) and (start_number % 4 !=0)):
	print("Congrats " + str(start_number) + "is an even number")
	
else:
	print("Congrats " + str(start_number) + "is an odd number")
	
print("----------------------------------------------------------------")

num = input("Now the fun begins enter a number champ!!")
num = int(num)

check = input("now divide by?")
check = int(check)

if(num % check == 0):
	print("Yay that divides you know the math real good huh")
	
else:
	print("Uh oh this aint looking very whole champ")
	
	 

