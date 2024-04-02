MA_NOTE = int(input("Entrez votre moyenne."))

if MA_NOTE < 12:
    print("Mention : Pas de mention")
elif 12 <= MA_NOTE < 14:
    print("Mention : Assez bien")
elif 14 <= MA_NOTE and MA_NOTE < 16:
    print("Mention : Bien")
elif 16 <= MA_NOTE < 18:
    print("Mention : Très bien")
elif 18 <= MA_NOTE <= 20:
    print("Mention : Les Félicitations du jury")
else:
    print("Votre moyenne ne peut être supérieur à 20.")