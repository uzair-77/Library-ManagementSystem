
# Library Management System

## Overview

The Library Management System is a simple console-based application that allows faculty and students to manage library books. The system supports various functionalities such as issuing books, adding new books, removing books, modifying book details, returning books, and searching for available books.

## Features

1. **Faculty Login**
   - Faculty members can log in using their credentials.
   - They have additional permissions to add, remove, and modify books.

2. **Student Login**
   - Students can log in using their credentials.
   - They can only issue and return books, and search for available books.

3. **Book Management**
   - **Issue a Book**: Faculty and students can issue a book if it is available.
   - **Add a Book**: Only faculty can add new books to the library.
   - **Remove a Book**: Only faculty can remove books from the library.
   - **Modify a Book**: Only faculty can modify the details of an existing book.
   - **Return a Book**: Books that have been issued can be returned to the library.
   - **Search for Books**: Users can search for books by title, author, or subject.
   - **Display Available Books**: Shows all available books in the library, optionally sorted by title or author.

## How It Works

1. **Login**
   - When the program starts, users are prompted to select their role (faculty or student).
   - Based on the role, users must log in with their username and password. Faculty have the option to manage books, while students can only issue and return books.

2. **Menu Options**
   - After successful login, users can choose from the following options:
     - **Issue a Book**: Enter the title or a keyword of the book to be issued.
     - **Add a Book**: (Faculty only) Enter details of the new book to be added to the library.
     - **Remove a Book**: (Faculty only) Enter the title of the book to be removed.
     - **Modify a Book**: (Faculty only) Enter the title of the book to be modified along with updated author or subject details.
     - **Search for Books**: Enter a search term to find books by title, author, or subject.
     - **Display Available Books**: List all books that are currently available. Optionally sort the list by title or author.
     - **Return a Book**: Enter the title of the book to return it to the library.

3. **Program Output**
   - The system provides feedback for each action, such as confirming the issuance of a book, notifying about the addition, removal, or modification of a book, and displaying search results or available books.

## Example

### Issuing a Book

**Input:**
```
Enter the book title or a keyword: The Hobbit
```

**Output:**
```
Book 'The Hobbit' issued successfully.
```

### Adding a Book (Faculty Only)

**Input:**
```
Enter the book title to add: The Great Gatsby
Enter the author name: F. Scott Fitzgerald
Enter the book subject: Classic
```

**Output:**
```
Book 'The Great Gatsby' already exists in the library.
```

### Removing a Book (Faculty Only)

**Input:**
```
Enter the book title to remove: The Da Vinci Code
```

**Output:**
```
Book 'The Da Vinci Code' removed from the library.
```

### Searching for Books

**Input:**
```
Enter the search term: Dystopian
```

**Output:**
```
Search results for 'Dystopian':
- 1984 by George Orwell (Dystopian)
- Brave New World by Aldous Huxley (Dystopian)
```

### Displaying Available Books

**Input:**
```
Sort books by (title/author) [press Enter for default ordering]:
```

**Output:**
```
Available Books:
- 1984 by George Orwell (Dystopian)
- Brave New World by Aldous Huxley (Dystopian)
- Fahrenheit 451 by Ray Bradbury (Science Fiction)
- Moby Dick by Herman Melville (Adventure)
- Pride and Prejudice by Jane Austen (Romance)
- The Alchemist by Paulo Coelho (Adventure)
- The Catcher in the Rye by J.D. Salinger (Coming-of-Age)
- The Hobbit by J.R.R. Tolkien (Fantasy)
- The Great Gatsby by F. Scott Fitzgerald (Classic)
```

## Requirements

- Python 3.x

## Running the Program

1. Save the code in a file named `books.py`.
2. Run the program using the command:
   ```bash
   books.py
   ```

3. Follow the prompts to interact with the system.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

