class Toto:
    def __init__(self, age: int):
        self.age = age


    def estMajeur(self):
        if self.age >= 18:
            return True
        return False
    
obj = Toto(20)

majeur = obj.estMajeur()
print(majeur)

