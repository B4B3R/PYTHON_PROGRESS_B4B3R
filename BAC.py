MA_NOTE = int(input("Entrez votre moyenne."))

if MA_NOTE < 12:
    print("Mention : Pas de mention")
elif MA_NOTE >= 12:
    print("Mention : Assez bien")
elif MA_NOTE >= 14:
    print("Mention : Bien")
elif MA_NOTE >= 16:
    print("Mention : Très bien")
elif MA_NOTE >= 18:
    print("Mention : Les Félicitations du jury")