from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home/value/{var}/")
async def root2(var):
    a = var*2
    return {"message": a}

