# if you want a pizza run this little program

my_table = []
my_wallet = 13.5
print("Respond with yes or no")
print("You have " + str(my_wallet) + " dollars in your wallet")
question = str(input("Do you want a pizza ?"))

if question == "yes":
    pizza_question = str(input("Which pizza do you want ?"))
    if pizza_question == "Salmone Pizza":
        print("Give me 10.5 dollars, please")
        my_wallet -= 10.5
        print("One pizza salmone for this table.")
        my_table.append("pizza salmone")
    elif pizza_question == "Sicilian Pizza":
        print("Give me 10.5 dollars, please")
        my_wallet -= 10.5
        print("One Sicilian Pizza  for this table.")
        my_table.append("Sicilian Pizza")
    elif pizza_question == "Roman Pizza":
        print("Give me 10.5 dollars, please")
        my_wallet -= 10.5
        print("One Roman Pizza for this table.")
        my_table.append("Roman Pizza")
    else:
        print("We just have the :\n     -Roman Pizza\n      -Sicilian Pizza\n       -Salmone Pizza") 
elif question == "no":
    print("Ok, what are you doing in that restaurant.")
else:
    print("Please respond with yes or no")

print("You have " + str(my_wallet) + " dollars in your wallet")

