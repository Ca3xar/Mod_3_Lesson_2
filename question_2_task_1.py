library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, title, author):
    new_book = (title, author)
    if new_book in library:
        print(f"The book {title} by {author} already exists.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added.")

add_book(library, "The Road", "Cormac McCarthy")
add_book(library, "1984", "George Orwell")
add_book(library, "Lord of the Rings", "J.R.R. Tolkien")


print("Updated Library: ")
for book in library:
    print(book)