def recherche(tab,n):
    if n in tab:
        return print(len(tab) - 2) # car l'indice du premier élément = 0
    else:
        return print(len(tab))

recherche([5,3],1)
recherche([2,4],2)
recherche([2,3,5,2,4],2)

# : permet de spécifier le type de notre variable
#  exemple d'usage
x = 0 
x:int 
# len() --> permet de renvoyer le nombre d'objets dans une list
# range() : methode qui va parcourir