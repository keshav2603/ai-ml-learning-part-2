class Library:
    books =[]
    numberOfBooks =0

    def addBookInLib(self, book):
        self.books.append(book)
        self.numberOfBooks =self.numberOfBooks+1 

l1=Library()
l1.addBookInLib("gita")
l1.addBookInLib("python")
l1.addBookInLib("java")
print(l1.numberOfBooks)
print(l1.books)