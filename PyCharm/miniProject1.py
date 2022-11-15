# ----------this is mini proj 1- Online Library Management System------------#

# create a library class
#     create methods/fns - display book,
#     2.lend book - inform person who owns the book if not present in library
#     3.add book,
#     4.return book
# obj :
# HarryLibrary = Library(listofbooks, library_name) - constructor

# create a main fun and run infinite while loop asking users for their input- input for what action they need?
# it will be out of 4 above methods


# we can maintain dictionary - which will have data on who has taken which book
# dict - key :books and value: nameofperson

class Library:
    ''' #docstring
    This is Online Library Management System. We are defining 4 activities.
    '''

    # global lendedBooks #NOTE - adhi me class var banavlela, pan better approach is to keep instance var
    # jo apan constructor madhe define kela like harry did
    # lendedBooks = {}
    def __init__(self, listofbooks, library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.lendedBooks = {} #followed like harry, made instance var

    def displayBooks(self):
        print(f'available books are:')
        for i in range(len(self.listofbooks)):
            print(self.listofbooks[i], end='\t')

    def lendBooks(self):
        # lendedBooks = {} #hyane jeva method run complete honar variable baher use nai honar
        username = input(f'\n Pl enter username: ')
        whichBook = input('Pl tell us which book are u looking for: ')
        if whichBook in self.listofbooks:
            print(f"Lended {whichBook} to {username}.")
            self.lendedBooks.update({whichBook: username})
            self.listofbooks.remove(whichBook)
        else:
            print('sorry for inconvenience. This book is not available.')
        #for lendBooks harry has used different approach, using dictry, can check out on his page
    def addBooks(self):
        print('Pl enter name of the book to be added:')
        booktobeadded = input()
        self.listofbooks.append(booktobeadded)
        print('added to library! ty.')

    def returnBooks(self):
        print('Pl enter name of book to be returned :')
        returnedBook = input()
        self.listofbooks.append(returnedBook)
        if returnedBook in self.lendedBooks:
            self.lendedBooks.pop(returnedBook)


booklist = ['b1', 'b2', 'b2', 'b3', 'b4', 'b4', 'b5', 'b6', 'b6', 'b7', 'b8', 'b9',
            'b9', 'b9', 'b10', 'b1', 'b7', 'b5', 'b5', 'b5']
juiLibrary = Library(booklist, 'Jui')

if __name__ == '__main__': #NOTE- JUST TYPE MAIN N NOT NAME
    while True:
        print(f"Welcome to the {juiLibrary.library_name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2', '3','4']:
            print('Invalid input, Pl enter a valid option')
            continue

        user_choice = int(user_choice) #adhi vertich int convert kertana jer str input dila ter int cha error yet hota
        # hence nanter int convert kela ;D so easy!
        if user_choice == 1:
            juiLibrary.displayBooks()
        elif user_choice == 2:
            juiLibrary.lendBooks()
            # print(juiLibrary.lendBooks().items())
        elif user_choice == 3:
            juiLibrary.addBooks()
        elif user_choice == 4:
            juiLibrary.returnBooks()
        # print(juiLibrary.lendBooks().items())
            print(juiLibrary.listofbooks)
        else:
            print('not a valid option')

        print('''press 'q' to quit or "c" to continue''')
        userChoice2 =''
        while(userChoice2!= 'q' and userChoice2!= 'c'):
            userChoice2 = input().lower()

            if userChoice2 == 'q':
                exit()
            elif userChoice2== 'c':
                continue



