import os


def add_book(title, genre, author):
    with open("books.txt", "a") as file:
        file.write(title + "/" + genre + "/" + author + "\n")
    print("本を追加しました\n")

def search_books():
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            books = file.readlines()
            for index, book in enumerate(books, start=1):#Back to here later.
                if search_word in books:
                    print(f"{book.strip()}\n")

def list_books():
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            books = file.readlines()
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book.strip()}\n")
    else:
        print("本がありません\n")

def main():
    choice = 0
    while choice !=4:
        print("蔵書キーパー")
        print("1. 本を追加")
        print("2. 本を検索")
        print("3. 本をすべて表示")
        print("4. 終了")
        choice = int(input("使いたい機能の数字を入力してください: "))
        
        if choice == 1:
            print("\n本を追加: 本の情報を追加してください")
            title = input("タイトル: ")
            genre = input("ジャンル: ")
            author = input("著者: ")
            add_book(title, genre, author)
            
        elif choice == 2:
            print("\n本を検索: 追加した本の検索ができます")
            search_word = input("タイトル、ジャンル、著者のいずれかを入力してください: ")
            search_books(search_word)#Back to here later.
            
        elif choice == 3:
            print("\n本をすべて表示: 追加した本をすべて表示します")
            list_books()
            
        else:
            choice == 4
            print("蔵書キーパーを終了しました")

if __name__ == "__main__":
    main()

