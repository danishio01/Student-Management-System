class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def display(self):
        print(f"Name: {self.name}, Taste: {self.taste}")
class Sweet(Food):
    def __init__(self, name):
        super().__init__(name, "Sweet")

s1 = Food("Pizza", "Savory")
s2 = Food("Ice Cream", "Sweet")
s3 = Sweet("Candy")

s1.display()
s2.display()
s3.display()