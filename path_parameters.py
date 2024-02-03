from fastapi import FastAPI
app = FastAPI()
Books = [
    {'title' : 'title one', 'author': 'author two','category': 'sceince'},
    {'title' : 'title two', 'author': 'author two' , 'category': 'sceince'},
    {'title' : 'title three', 'author': 'author two','category': 'sceince'},
    {'title' : 'title four', 'author': 'author two','category': 'sceince'},
    {'title' : 'title five', 'author': 'author two','category': 'sceince'}
]
@app.get("/")
async def first_api_books():
    return {'message': "hello bharathi"}

@app.get("/books")
async def first_api_books():
    return Books

@app.get("/books/mybooks")
async def first_api_books():
    return {'it returns': 'my favourite book'}

@app.get("/books/{book_title}")
async def first_api_books(book_title : str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book


