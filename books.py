import typing
import fastapi
import enum

app = fastapi.FastAPI()

BOOKS = {
    "book1" : { "name" : "Title One", "author" : "Author One"},
    "book2" : { "name" : "Title Two", "author" : "Author Two"},
    "book3" : { "name" : "Title Three", "author" : "Author Three"},
    "book4" : { "name" : "Title Four", "author" : "Author Four"},
    "book5" : { "name" : "Title Five", "author" : "Author Five"},
}

# Get all books
@app.get("/")
async def readAllBooks(skip_book: typing.Optional[str] = None):

    # If skip_book is not defined return original
    if not skip_book:
        return BOOKS

    # If it is defined return newBooks (copy of BOOKS) after deleting the skip_book entry
    newBooks = BOOKS.copy()
    del newBooks[skip_book]
    return newBooks

# Get specific book ex: book_id = book1
@app.get("/")
async def readBook(book_id: str):
    return BOOKS[book_id]

# Create new book
@app.post("/")
async def create_book(book_title: str, book_author: str):
    lenOfBooks: int = len(BOOKS)
    if lenOfBooks == 0:
        BOOKS["book1"] = {"name": book_title, "author": book_author}
    else:
        largestBookId = 0
        for book in BOOKS:
            largestBookId = max(int(book[-1]), largestBookId)
        BOOKS[f"book{largestBookId+1}"] = {"name": book_title, "author": book_author}        
        return {BOOKS[f"book{largestBookId+1}"]}

# Update existing book
@app.put("/")
async def update_book(book_id: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_id] = book_information
    return book_information

@app.delete("/")
async def update_book(book_id: str):
    del BOOKS[book_id]    
    return BOOKS
