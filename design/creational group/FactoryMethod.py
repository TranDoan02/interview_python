class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]

pet = get_pet("cat")
print(pet.speak())  # Meow!
