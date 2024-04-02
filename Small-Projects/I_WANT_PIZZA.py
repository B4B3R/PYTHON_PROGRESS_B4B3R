# if you want a pizza run this little program

my_table = []
my_wallet = 13.5
print("Respond with yes or no")
print("You have " + str(my_wallet) + " dollars in your wallet")
counter = 0

while counter < 3:
    
    question = str(input("Do you want a pizza ?     ")) # the question is inside the loop because you need to "refresh" the loop

    if question == "yes":

        pizza_question = str(input("Which pizza do you want ?   "))

        if pizza_question == "Salmone Pizza":

            print("Give me 10.5 dollars, please")
            my_wallet -= 10.5
            print("One pizza salmone for this table.")
            my_table.append("pizza salmone")
            counter += 1
            continue

        elif pizza_question == "Sicilian Pizza":

            print("Give me 10.5 dollars, please")
            my_wallet -= 10.5
            print("One Sicilian Pizza  for this table.")
            my_table.append("Sicilian Pizza")
            counter += 1
            continue

        elif pizza_question == "Roman Pizza":

            print("Give me 10.5 dollars, please")
            my_wallet -= 10.5
            print("One Roman Pizza for this table.")
            my_table.append("Roman Pizza")
            counter += 1
            continue

        else:

            print("We just have the :\n     -Roman Pizza\n     -Sicilian Pizza\n     -Salmone Pizza")
            counter += 1
            continue

    elif question == "no":

        print("Ok, what are you doing in that restaurant.")
        break

    else:

        print("Please respond with yes or no")
        continue

print("You have " + str(my_wallet) + " dollars in your wallet")
print("In your table you have, " + str(my_table))
print(counter)
