class BookStore:
    NoOfBooks = 0
    def __init__(self,BookName, Author):
        self.BookName = BookName
        self.Author = Author
        BookStore.NoOfBooks += 1
    
    def Display(self):
        print(f"{self.BookName} by {self.Author}. No of Books : {self.NoOfBooks}")


obj1 = BookStore("Linux System Programing", "Robert Love")
obj1.Display()
obj2 = BookStore("C Programing", "Dennies Ritchie")
obj2.Display()

