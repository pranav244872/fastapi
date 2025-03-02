"""Used to generate unique ids for book object"""

import uuid
import typing
import pydantic
import fastapi

app = fastapi.FastAPI()


class Book(pydantic.BaseModel):
    """Book object"""

    id: uuid.UUID
    title: str = pydantic.Field(min_length=1, max_length=100)
    author: str = pydantic.Field(min_length=1, max_length=100)
    description: typing.Optional[str] = pydantic.Field(
        title="Description of the book", max_length=100, min_length=1
    )
    rating: int = pydantic.Field(gt=0, l=11)

    class Config:
        json_schema_extra = {
            "example": {
                "id": uuid.uuid4(),
                "title": "Computer Science Pro",
                "author": "Codingwithroby",
                "description": "A very nice description of a book",
                "rating": 7,
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books(books_to_return: typing.Optional[int] = None):
    """Returns all books"""
    if len(BOOKS) < 1:
        create_books_no_api()

    if not ((books_to_return) and (len(BOOKS) >= books_to_return > 0)):
        return BOOKS

    new_books = []

    for i in range(books_to_return):
        new_books.append(BOOKS[i])

    return new_books


@app.post("/")
async def create_book(book: Book):
    """Creates a new book"""
    BOOKS.append(book)
    return book


def create_books_no_api():
    """Creates 4 new books without an api (For testing)"""
    book1 = Book(
        id=uuid.uuid4(),
        title="Title 1",
        author="Author 1",
        description="Description 1",
        rating=6,
    )
    book2 = Book(
        id=uuid.uuid4(),
        title="Title 2",
        author="Author 2",
        description="Description 2",
        rating=7,
    )
    book3 = Book(
        id=uuid.uuid4(),
        title="Title 3",
        author="Author 3",
        description="Description 3",
        rating=8,
    )
    book4 = Book(
        id=uuid.uuid4(),
        title="Title 4",
        author="Author 4",
        description="Description 4",
        rating=9,
    )
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)
