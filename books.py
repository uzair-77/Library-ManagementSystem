class LibraryManagementSystem:
    def __init__(self):
        self.faculty_users = {'Syed Uzair: '567643'}  # Sample faculty credentials
        self.student_users = {'Gillani': '456'}  # Sample student credentials
        self.books = [
            {'title': '1984', 'author': 'George Orwell', 'subject': 'Dystopian', 'status': 'available'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'subject': 'Romance', 'status': 'available'},
            {'title': 'Moby Dick', 'author': 'Herman Melville', 'subject': 'Adventure', 'status': 'available'},
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'subject': 'Classic', 'status': 'available'},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'subject': 'Coming-of-Age', 'status': 'available'},
            {'title': 'Brave New World', 'author': 'Aldous Huxley', 'subject': 'Dystopian', 'status': 'available'},
            {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'subject': 'Fantasy', 'status': 'available'},
            {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'subject': 'Science Fiction', 'status': 'available'},
            {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'subject': 'Adventure', 'status': 'available'},
            {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'subject': 'Thriller', 'status': 'available'}
        ]

    def faculty_login(self):
        login_attempts = 0
        while login_attempts < 3:
            username = input("Enter your faculty username: ")
            password = input("Enter your faculty password: ")
            if self.authenticate_faculty(username, password):
                print("Faculty login successful!")
                return 'faculty'
            else:
                print("Invalid faculty username or password. Please try again.")
                login_attempts += 1
        print("Too many login attempts. Exiting...")
        exit()

    def student_login(self):
        login_attempts = 0
        while login_attempts < 3:
            username = input("Enter your student username: ")
            password = input("Enter your student password: ")
            if self.authenticate_student(username, password):
                print("Student login successful!")
                return 'student'
            else:
                print("Invalid student username or password. Please try again.")
                login_attempts += 1
        print("Too many login attempts. Exiting...")
        exit()

    def authenticate_faculty(self, username, password):
        if username in self.faculty_users and self.faculty_users[username] == password:
            return True
        return False

    def authenticate_student(self, username, password):
        if username in self.student_users and self.student_users[username] == password:
            return True
        return False

    def issue_book(self, book_title):
        matching_books = [book for book in self.books if book_title.lower() in book['title'].lower()]
        if matching_books:
            for book in matching_books:
                if book['status'] == 'available':
                    book['status'] = 'issued'
                    print(f"Book '{book['title']}' issued successfully.")
                    return
            print(f"Book '{book_title}' is currently not available.")
        else:
            print(f"No books found with the title '{book_title}'.")

    def add_book(self, book_title, author, subject):
        if any(book['title'].lower() == book_title.lower() for book in self.books):
            print(f"Book '{book_title}' already exists in the library.")
        else:
            new_book = {
                'title': book_title,
                'author': author,
                'subject': subject,
                'status': 'available'
            }
            self.books.append(new_book)
            print(f"Book '{book_title}' added to the library.")

    def remove_book(self, book_title):
        for book in self.books:
            if book['title'].lower() == book_title.lower():
                self.books.remove(book)
                print(f"Book '{book_title}' removed from the library.")
                return
        print(f"Book '{book_title}' does not exist in the library.")

    def modify_book(self, book_title, author=None, subject=None):
        for book in self.books:
            if book['title'].lower() == book_title.lower():
                if author:
                    book['author'] = author
                if subject:
                    book['subject'] = subject
                print(f"Book '{book_title}' modified successfully.")
                return
        print(f"Book '{book_title}' does not exist in the library.")

    def return_book(self, book_title):
        matching_books = [book for book in self.books if book_title.lower() in book['title'].lower()]
        if matching_books:
            for book in matching_books:
                if book['status'] == 'issued':
                    book['status'] = 'available'
                    print(f"Book '{book['title']}' returned successfully.")
                    return
            print(f"Book '{book_title}' is not currently issued.")
        else:
            print(f"No books found with the title '{book_title}'.")

    def search_books(self):
        search_term = input("Enter the search term: ")
        found_books = []
        for book in self.books:
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower() or search_term.lower() in book['subject'].lower():
                found_books.append(book)
        if found_books:
            print(f"Search results for '{search_term}':")
            for book in found_books:
                print(f"- {book['title']} by {book['author']} ({book['subject']})")
        else:
            print(f"No books found for '{search_term}'.")

    def sort_books(self, sort_by=None):
        if sort_by == 'title':
            sorted_books = sorted(self.books, key=lambda x: x['title'])
        elif sort_by == 'author':
            sorted_books = sorted(self.books, key=lambda x: x['author'])
        else:
            sorted_books = self.books

        return sorted_books

    def display_books(self, sort_by=None):
        sorted_books = self.sort_books(sort_by)
        print("Available Books:")
        for book in sorted_books:
            if book['status'] == 'available':
                print(f"- {book['title']} by {book['author']} ({book['subject']})")

    def start(self):
        user_type = input("Select the type of a user :\n1. Faculty login\n2. Student login\nEnter the choice of the user: ")

        if user_type == '1':
            user_role = self.faculty_login()
        elif user_type == '2':
            user_role = self.student_login()
        else:
            print("Invalid choice. Exiting...")
            return

        while True:
            print("\nMenu:")
            print("1. Issue a book")
            if user_role == 'faculty':
                print("2. Add a book")
                print("3. Remove a book")
                print("4. Modify a book")
            print("5. Search for books")
            print("6. Display available books")
            print("7. Return a book")  # New option for returning a book
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                book_title = input("Enter the book title or a keyword: ")
                self.issue_book(book_title)

            elif choice == '2' and user_role == 'faculty':
                book_title = input("Enter the book title to add: ")
                author = input("Enter the author name: ")
                subject = input("Enter the book subject: ")
                self.add_book(book_title, author, subject)
            elif choice == '3' and user_role == 'faculty':
                book_title = input("Enter the book title to remove: ")
                self.remove_book(book_title)
            elif choice == '4' and user_role == 'faculty':
                book_title = input("Enter the book title to modify: ")
                author = input("Enter the updated author name (press Enter to skip): ")
                subject = input("Enter the updated book subject (press Enter to skip): ")
                self.modify_book(book_title, author, subject)
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                sort_by = input("Sort books by (title/author) [press Enter for default ordering]: ")
                self.display_books(sort_by)
            elif choice == '7':
                book_title = input("Enter the book title to return: ")
                self.return_book(book_title)  # Calling the new return_book method
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


library_system = LibraryManagementSystem()
library_system.start()
