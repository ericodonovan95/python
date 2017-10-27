# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 
# Extras:
# 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.



name = input("Please enter your name")

age = input("please enter your age")
age = int(age)

get_centeniary = 2017 + (100 - age)

print("Ok " +  name + " you will turn 100 in " + str(get_centeniary))

new_number = input("Enter another number i dare you")
new_number= int(new_number)
counter = 1


while(new_number >= counter):
    print("Ok " +  name + " you will turn 100 in " + str(get_centeniary))
    counter += 1
        