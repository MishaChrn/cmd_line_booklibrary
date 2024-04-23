import os
#search_books function is added.
#menu1-4 are re-tested.
#EN version is created based on JA version Apr. 24

def add_book(title, genre, author):
    with open("books_EN.txt", "a") as file:
        file.write(title + " / " + genre + " / " + author + "\n")
    print("The book is added to the list successfully.\n")

def search_books(search_word):
    if os.path.exists("books_EN.txt"):
        with open("books_EN.txt", "r") as file:
            books = file.readlines()
    search_result = [books for books in books if search_word in books]
    for books in search_result:
        print("\n" + books)

def list_books():
    if os.path.exists("books_EN.txt"):
        with open("books_EN.txt", "r") as file:
            books = file.readlines()
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book.strip()}\n")
    else:
        print("You haven't added books yet.\n")

def main():
    choice = 0
    while choice !=4:
        print("Library Keeper")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Show Book List")
        print("4. Exit")
        choice = int(input("Input the menu index (1-4): "))
        
        if choice == 1:
            print("\nAdd Book: Input book's information.")#Want to add 'back to menu' button
            title = input("Title: ")
            genre = input("Genre: ")
            author = input("Author: ")
            add_book(title, genre, author)
            
        elif choice == 2:
            print("\nSearch Books: Find your books by a key word.")
            search_word = input("Input book's title, genre, or author: ")#Want to enable multi-word search
            search_books(search_word)
            
        elif choice == 3:
            print("\nShow Book List: Look through the books you've added.")
            list_books()
            
        else:
            choice == 4
            print("Library Keeper is closed.")

if __name__ == "__main__":
    main()

