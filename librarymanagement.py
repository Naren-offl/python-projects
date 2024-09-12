import copy
class Library():
    def __init__(self,list):
        self.books_list = copy.deepcopy(list)
        self.available_books_list = copy.deepcopy(list)
        self.books_lent={} #key:book  --  value-user_name
    def display_available_books(self):
        for book in self.available_books_list:
            print(book)
    def display_all_books(self):
        for book in self.books_list:
            print(book)
    def lend_book(self,name,book):
        if book not in self.books_list:
            print("Incorrect book Name , Please check book list")
            return
        if book in self.available_books_list:
            self.books_lent[book]=name #self.book_lent.update({book:name})
            self.available_books_list.remove(book)
            print("you can take the book")
        else:
            print("the book is already taken by "+self.books_lent[book])

    def return_book(self,book):
        del self.books_lent[book]
        self.available_books_list.append(book)


if __name__ == "__main__":
    lib = Library(["To Kill a Mockingbird","1984","Pride and Prejudice", "The Great Gatsby","Moby-Dick"])
    print("Welcome to library Management System!!!")
    while 1:
        print("*" * 40)
        print("1.Display Available books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")
        user_choice = int(input("Enter your choice:-"))
        print("*"*40)
        if user_choice == 1:
            lib.display_available_books()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            name = input("Enter your Name:")
            book = input("Enter book Name:")
            lib.lend_book(name,book)
        elif user_choice == 4:
            book = input("Enter the name of book:-")
            lib.return_book(book)
        elif user_choice == 5:
            print("Thank you for Visiting!!!")
            break
        else:
            print("User Choice Invalid!!!")
