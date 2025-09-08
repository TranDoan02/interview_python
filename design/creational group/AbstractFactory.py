class Dog():
    def speak(self):
        return "Woof!"

class DogFactory():
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "Dog Food"

class PetShop():
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        food = self.pet_factory.get_food()
        print(f"Our pet says {pet.speak()} and eats {food}")

shop = PetShop(DogFactory())
shop.show_pet()  # Our pet says Woof! and eats Dog Food
#Tạo ra nhiều họ đối tượng liên quan hoặc phụ thuộc mà không cần chỉ rõ lớp cụ thể; 
# thích hợp cho hệ thống cần linh hoạt theo môi trường hoặc cấu hình.