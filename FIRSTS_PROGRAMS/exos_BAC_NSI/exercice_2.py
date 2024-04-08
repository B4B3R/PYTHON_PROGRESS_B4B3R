def max_et_indice(tab:list):
    indice = 0
    for i in range(len(tab)): # on parcourt par indice / for i donc par indice /for e 
        max_actuel = 0
        if tab[i] > max_actuel:
            max_actuel = tab[i]
            i = len(tab[i]) - 1

    return print(tuple_max_et_indice = (max_actuel, indice))

max_et_indice([1,5,6,9,1,2,3,7,9,8])
