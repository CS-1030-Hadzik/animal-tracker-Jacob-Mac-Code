from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    # TODO: Initialize the Dog class and add the breed attribute.
    # The constructor should accept name, species, and breed as parameters.
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    
    
    def __str__(self):
        return super().__str__() + f", Breed: '{self.breed}'"


    def speak(self):
        print("The dog barks.")
