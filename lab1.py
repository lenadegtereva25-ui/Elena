class Book:
    def init(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def str(self):
        return f'Книга "{self.name}"'

    def repr(self):
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"