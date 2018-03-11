#get user email address
email = input("What is your email address").strip()

#slice out username

user = email[0:email.index("@"):1]

#slice out domain name
domain = email[email.index("@"):].strip("@")
# format message
output = "Your username is {} and your domain name is {}"
message = output.format(user , domain)
print(message)
#display output messsage

