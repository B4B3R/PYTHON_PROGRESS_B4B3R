# word guessing game

lifes = 7
word = "BONJOUR"
list_of_your_letters = []

while lifes > 0:
    
    your_letter = str(input("Selectionner une lettre    "))
    print("Il vous reste " + str(lifes) + " vies.")
    print("Vous avez saisi les lettres :    \n" + str(list_of_your_letters) )

    if your_letter in word or your_letter in word.lower():
    
        print("You have one letter right ! ")
        list_of_your_letters.append(your_letter)
        
    
    elif str(list_of_your_letters) in word:
    
        print("Vous avez trouvez toutes les lettres")
        break
    
    
    elif your_letter == "":

        print("--------")
    
    else:
        
        print("There is not that letter")
        list_of_your_letters.append(your_letter)
        lifes -= 1
