from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

def list_library_books(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

def get_library_librarian(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage:
if __name__ == "__main__":
    # Create sample data
    author = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(title="Harry Potter", author=author)
    library = Library.objects.create(name="Central Library")
    library.books.add(book)
    librarian = Librarian.objects.create(name="John Doe", library=library)

    # Test queries
    print("Books by J.K. Rowling:", query_books_by_author("J.K. Rowling"))
    print("Books in Central Library:", list_library_books("Central Library"))
    print("Central Library's librarian:", get_library_librarian("Central Library"))
