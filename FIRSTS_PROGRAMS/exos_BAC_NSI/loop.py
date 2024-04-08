liste = [0,3,1,5,7,8]
chaine = "Salut, je suis B4B"

for e in liste:
for i in range(len(liste))
for caractere in chaine:

for e in quelquechose: # pour chaque élément dans quelque chose 
for i in range() # pour chaque indice dans range
for caractere in chaine: # pour chaque caractère dans une chaine à l'intérieur de notre variable chaine

# exemple de fonction récursive : fonction qui se rappelle elle meme
def test(coucou:int)->int:
  while 2-1==1:
    return test(coucou+1)

def max_et_indice(tab:list)->int:
    maximum = tab[0]
    if len(tab) == 0:
        return (0,0)
    if len(tab) == 1:
        return (tab[0],0)
    for i in range(len(tab)):
        if maximum < tab[i]:
            maximum = tab[i]
    for k in range(len(tab)):
        if tab[k] == maximum:
            return (maximum,k)

# Vérifier si ton code génère une erreur, et, si c'est le cas, prévoir:

try:
  print(x)
except:
  print("La variable x n'est pas définie.")