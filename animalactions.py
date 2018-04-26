class AnimalActions:
    def quack(self): return self.strings["quack"]
    def feathers(self): return self.strings["feathers"]
    def bark(self): return self.strings["bark"] 
    def fur(self): return self.strings["fur"]

class Duck(AnimalActions):
    strings = dict(
        quack = "Quack!",
        feathers = "the duck has grey feathers",
        bark = "the duck cannot bark",
        fur = "the duck has no fur"
        )
class Person(AnimalActions):
    strings = dict(
        quack = "person does not make duck sounds",
        feathers = "the person picks up a feather",
        bark = "the person barks like a dog",
        fur = "the person has no fur"
        )

class Dog(AnimalActions):
    strings = dict(
        quack = "dog does not make duck sounds",
        feathers = "the dog finds a feather",
        bark = "Woof woof",
        fur = "the dog has thick fur"
        )
    
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("In the forest: ")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("In the doghouse: ")
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__": main()
