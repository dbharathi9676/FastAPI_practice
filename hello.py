from fastapi import FastAPI
app = FastAPI()
@app.get("/" , description="ths is my first route" , deprecated=False)
async def hello_api():
    return {"message" : "hello bharathi priya"}

@app.post("/")
async def post():
    return{"message": "hello from the post route" }

@app.put("/")
async def put():
    return{"message": "hello from the put route"}