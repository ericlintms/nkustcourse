class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

class Ebook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def display_info(self):
        book_info = super().display_info()
        return f"{book_info}, Format: {self.file_format}"

# 範例
my_book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
my_ebook = Ebook("The Hobbit", "J.R.R. Tolkien", 310, "PDF")

print(my_book.display_info())
print(my_ebook.display_info())
