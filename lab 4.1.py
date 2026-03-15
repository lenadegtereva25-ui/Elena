if __name__ == "__main__":

    class Animal:

        def __init__(self, name: str, species: str, age: int):

            self.name = name
            self.species = species
            self.age = age

        def make_sound(self) -> str:
            
            return "Неизвестный звук"

        def __str__(self) -> str:
           
            return f"{self.name} — {self.species}, возраст: {self.age} лет"

        def __repr__(self) -> str:
          
            return f"Animal(name='{self.name}', species='{self.species}', age={self.age})"


    class Dog(Animal):
        
        def __init__(self, name: str, age: int, breed: str):
           
            super().__init__(name, "Собака", age)  # species фиксируем как "Собака"
            self.breed = breed  # новый атрибут для породы

        def make_sound(self) -> str:
            
            return "Гав-гав!"

        def fetch_stick(self) -> str:
        
            return f"{self.name} принесла палку!"

    class Cat(Animal):
        

        def __init__(self, name: str, age: int, color: str):
            
            super().__init__(name, "Кошка", age)  # species фиксируем как "Кошка"
            self.color = color  # новый атрибут для цвета шерсти

        def make_sound(self) -> str:
           
            return "Мяу!"

        def climb_tree(self) -> str:
        
            return f"{self.name} залезла на дерево!"