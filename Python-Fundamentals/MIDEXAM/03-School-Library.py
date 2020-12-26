# 03. School Library

def check_book_exist(books_list, book_searched):
    return True if book_searched in books_list else False


books = input().split("&")


command = input()
while not command == "Done":
    command_type = command.split(" | ")[0]

    if command_type == "Add Book":
        book_name = command.split(" | ")[1]
        if not check_book_exist(books, book_name):
            books.insert(0, book_name)
    elif command_type == "Take Book":
        book_name = command.split(" | ")[1]
        if check_book_exist(books, book_name):
            books.remove(book_name)
    elif command_type == "Insert Book":
        book_name = command.split(" | ")[1]
        books.append(book_name)
    elif command_type == "Swap Books":
        book1 = command.split(" | ")[1]
        book2 = command.split(" | ")[2]
        if check_book_exist(books, book1) and check_book_exist(books, book2):
            index1 = books.index(book1)
            index2 = books.index(book2)
            books[index1] = book2
            books[index2] = book1
    elif command_type == "Check Book":
        index = int(command.split(" | ")[1])
        if 0 <= index < len(books):
            print(books[index])

    command = input()

print(', '.join(books))