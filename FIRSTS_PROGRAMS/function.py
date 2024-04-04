# codage de fonction

def my_function(x = 2):
    print("x =   " + str(x))

my_function(4)
my_function()

# introduction de la notion d'args et de kwargs

def function_args(*args):
    print("x =  ", *args)
    print("Pour info, *args a comme type :  ", type(args)) # class tuple introduite 


function_args(2,1,6,7)

def function_kwargs(**kwargs):
    print("x =  ", *kwargs)
    print("Pour info, *args a comme type :  ", type(kwargs)) # class dictionnary introduite 

function_kwargs(a=2,b=1,c=6,d=7)
# function_kwargs(2,1,6,7) cette ligne nous renverrait une erreur car vu que nous avons spécifié kwargs 
# nous devons attribuer à des variables nos valeurs et pas juste saisir des valeurs

def S(x, y):
    return print(x + y)

S(3,2)

# Notion de scope 

a = 0

def variable_1():
    # si on spécifie rien a = 0
    print(a)

def variable_1():
    a = 2
    print(a)

def variable_3():
    a = 3
    print(a)

