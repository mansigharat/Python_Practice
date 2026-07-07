from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get('/about')
def about():
    return {'message':'I am working hard for a better future.'}