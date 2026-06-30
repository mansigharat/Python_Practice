import json
from typing import Optional
from fastapi import FastAPI,Path,HTTPException
from pydantic import BaseModel,computed_field
from fastapi.responses import JSONResponse

app = FastAPI()

class Book(BaseModel):
    id : str
    name : str
    author : str
    total_copies : int
    borrowed_copies : int

    @computed_field
    @property
    def remain_copies(self)-> int:
        remain_copies = self.total_copies - self.borrowed_copies
        return remain_copies

    @computed_field
    @property
    def available(self)-> bool:
        if self.remain_copies == 0 :
            return False
        else:
            return True

class UpdateBook(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    total_copies: Optional[int] = None
    borrowed_copies: Optional[int] = None

def load_data():
    with open("books.json","r") as f:
        data = json.load(f)
    return data 

def save_data(data):
    with open("books.json", "w") as f:
        json.dump(data, f)

@app.get("/books")
def view_all_books():
    data = load_data()
    return data

@app.get("/books/{book_id}")
def view_single_book(book_id: str = Path(..., description="ID of the book in the database", examples=['B001'])):
    data = load_data()
    
    if book_id not in data:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return data[book_id]

@app.post("/create")
def create_book(book : Book):
    data = load_data()
    if book.id in data:
        raise HTTPException(status_code = 400,detail ='Book is already exists')
    
    data[book.id] = book.model_dump(exclude = ['id'])
    save_data(data)
    
    return {"message": "Book added successfully"}

@app.put("/update/{book_id}")
def update_details(book_id:str , update_book : UpdateBook):

    data = load_data()
    if book_id  not in data:
        raise HTTPException(status_code = 400,detail ='Book is not exists')
    
    exisiting_book_data = data[book_id]

    updated_book_data = update_book.model_dump(exclude_unset = True)

    for key,value in updated_book_data.items():
        exisiting_book_data[key] = value

    exisiting_book_data['id'] = book_id
    book_pydantic_obj = Book(**exisiting_book_data)
    exisiting_book_data = book_pydantic_obj.model_dump(exclude = {id})
    data[book_id] = exisiting_book_data

    save_data(data)

    return JSONResponse(status_code = 200 ,content={'message':'book updated'})

@app.delete('/delete/{book_id}')
def delete_book(book_id : str):
    data = load_data()

    if book_id not in data:
        raise HTTPException(status_code = 404 , detail = 'Book not found')
    
    del data[book_id]

    save_data(data)
    return JSONResponse(status_code = 200 ,content={'message':'Book Deleted'}) 