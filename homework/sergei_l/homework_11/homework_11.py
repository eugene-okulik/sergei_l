class Book:
    page_material = 'бумага'
    is_text = True

    def __init__(self, book_title, author, pages_qty, isbn, is_reserved):
        self.book_title = book_title
        self.author = author
        self.pages_qty = pages_qty
        self.isbn = isbn
        self.is_reserved = is_reserved


class SchoolBook(Book):

    def __init__(
            self, book_title, author, pages_qty, isbn, is_reserved, subject, school_class, is_tasks
    ):
        super().__init__(book_title, author, pages_qty, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.is_tasks = is_tasks


book_1 = Book('Идиот', 'Достоевский', 289, '23443-ID', False)
book_2 = Book(
    'Преступление и наказание', 'Достоевский', 324, '23886-ID', False
)
book_3 = Book('Война и мир', 'Толстой', 1242, '59086-TO', False)
book_4 = Book('Анна Каренина', 'Толстой', 423, '57436-TO', False)
book_5 = Book('Хаджи-Мурат', 'Толстой', 639, '59236-TO', True)
school_book_1 = SchoolBook(
    'Алгебра', 'Иванов', 139, '00236-IM', False,
    'Математика', 9, True
)
school_book_2 = SchoolBook(
    'Высшая математика', 'Иванов', 199, '00246-IM', False,
    'Математика', 11, True
)
school_book_3 = SchoolBook(
    'Физика', 'Иванов', 112, '00536-IM', True,
    'Физика', 5, True
)


def print_details(book):
    book_data_list = []
    book_data_list.append('Название: ' + book.book_title)
    book_data_list.append('Автор: ' + book.author)
    book_data_list.append('страниц: ' + str(book.pages_qty))
    if book.__class__ == Book:
        book_data_list.append('материал: ' + book.page_material)
    else:
        book_data_list.append('предмет: ' + book.subject)
        book_data_list.append('класс: ' + str(book.school_class))
    if book.is_reserved:
        book_data_list.append('зарезервирована')
    print(', '.join(book_data_list))


print_details(book_1)
print_details(book_2)
print_details(book_3)
print_details(book_4)
print_details(book_5)
print_details(school_book_1)
print_details(school_book_2)
print_details(school_book_3)
