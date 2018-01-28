class User:

    owned_books = list()
    overdue_books = dict()
    overdue_books.update()
    fines = 0
    name = ""
    phone_number = ""
    address = ""
    library_card_number = 0


    def set_name(self, new_name):
        User.name = new_name
        pass

    def set_phone_number(self, new_phone_number):
        User.phone_number = new_phone_number
        pass


    # 555555555555555555555555
    def add_fine_for_book(self, book_name):
        # inde =
        # if :

    def set_address(self, new_address):
        User.address = new_address
        pass


class Patron(User):


    def check_out_book(self, bok):
        User.owned_books.append(bok)
        pass


    def return_book(self, bok):
        User.owned_books.remove(bok)
        pass



    def search_for_a_book(self, list_of_all_books, looking_for):
        ind = list_of_all_books.index(looking_for)
        list_of_all_books
        pass



class Faculty(Patron):

    def renew_book(self, name_of_book):
        del User['name_of_book']
        pass



class Student(Patron):



class Librarian(User):

