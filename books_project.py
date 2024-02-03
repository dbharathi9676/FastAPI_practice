from fastapi import FastAPI
app = FastAPI()
Books = [
    {'title' : 'one', 'author': 'author two','category': 'sceince'},
    {'title' : 'one', 'author': 'author two','category': 'sceince'},
    {'title' : 'one', 'author': 'author two','category': 'sceince'},
    {'title' : 'one', 'author': 'author two','category': 'sceince'},
    {'title' : 'one', 'author': 'author two','category': 'sceince'}
]
@app.get("/books")
async def hello_api():
    return Books
