class Library:
    def init(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id: int):
        for index, book in enumerate(self.books):
            if book.id == id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")