# central concept for the POO

class Profil:
    def __init__(self, name, level, year): # initiation of a constructor to have a structure of any object of this class
        self.name = name
        self.level = level
        self.year = year

    def Presentation(self):
        print("That's me")
        


B4B3R = Profil("B4B",10,2000)

print(B4B3R.level)
B4B3R.level = 100
print(B4B3R.level)

B4B3R.Presentation()
print(dir(B4B3R))
