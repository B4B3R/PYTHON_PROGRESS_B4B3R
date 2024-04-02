# word guessing game

lifes = 7
word = "BONJOUR"
list_of_your_letters = []

while lifes > 0: # boucle pour arrêter le jeu quand le joueur n'aura plus de vies
    
    your_letter = str(input("Selectionner une lettre    "))
    print("Il vous reste " + str(lifes) + " vies.")
    print("Vous avez saisi les lettres :    \n" + str(list_of_your_letters) )

    if your_letter in word or your_letter in word.lower():
    
        print("You have one letter right ! ")
        list_of_your_letters.append(your_letter)
        
        for l in word or l in word.lower(): # boucle for pour selectionner chaque lettre du mot à trouver en minuscule et en majuscule
            if l in list_of_your_letters: # condition pour savoir quand le joueur aura trouver toutes les lettres
                    print("GG! Vous avez trouvé le mot qui était bonjour, ne vous inquiétez pas les majuscules et les minuscules n'ont eu aucune incidence sur le jeu.")
                    lifes = 0
            else:
                print("Vous n'avez toujours pas trouver le mot.")
                break

    else:
        
        print("There is not that letter")
        list_of_your_letters.append(your_letter)
        lifes -= 1

# Principes à appliquer pour améliorer le programme
# function: len(), range(), [] "mot_public[:3] + 'h' + mot_public[4:]"
#            enumerate(), break, validation de données, interface graphique