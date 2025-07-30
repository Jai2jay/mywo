
class book:
    category = 'bike' #class variable
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year   
    def book_info(self):
        print(f"title: {self.title}, author: {self.author},publication_year;{self.publication_year}")
# car = vehicle('suv',1000000)        
#         car.details()

class FictionBook(book):
     def __init__(self, title, author, publication_year,genre):
         super().__init__(title, author, publication_year)
         self.genre = genre
     def display_genre(self):
         super().book_info()
         print(f"genre: {self.genre}")

class NonFictionBook(book):
     def __init__(self, title, author, publication_year,subject):
         super().__init__(title, author, publication_year)
         self.subject = subject
     def display_subject(self):
         super().book_info()
         print(f"subject: {self.subject}")


book1= FictionBook('jai','jay',2007,'fiction')
book1.display_genre()

book2= NonFictionBook('meluha','jay','2015','biography')
book2.display_subject()