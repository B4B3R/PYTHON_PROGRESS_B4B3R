from random import *
    

nb_lifes = 7
unknow_word = 'B4B3R'
public_word = '_' * len(unknow_word)

while public_word != unknow_word and nb_lifes != 0:
    print("You have " + str(nb_lifes) + " lifes.")
    print('Word:      ' + public_word)
    letter = str(input("Enter your letter.      "))

    if letter in unknow_word:
        for l in range(len(public_word)):
            if unknow_word[l] == letter:
                public_word = public_word[:l] + letter + public_word[l+1:]
                print("BRAVO")
      
    else:
        nb_lifes -= 1

print("The game is finish.")

