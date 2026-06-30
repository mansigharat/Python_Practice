import json
from typing import Optional
from fastapi import FastAPI,Path,HTTPException
from pydantic import BaseModel,computed_field
from fastapi.responses import JSONResponse

app = FastAPI()

class Movie(BaseModel):
    id : str
    title : str
    director : str
    total_tickets : int
    booked_tickets : int


    @computed_field
    @property
    def available_tickets(self)->int:
        return self.total_tickets - self.booked_tickets
        
class UpdateMovie(BaseModel):
    title : Optional[str] = None
    director : Optional[str] = None
    total_tickets : Optional[int] = None
    booked_tickets : Optional[int] = None

def load_data():
    with open("movies.json","r") as f:
        return json.load(f)  

def save_data(data):
    with open("movies.json", "w") as f:
        json.dump(data, f)

@app.get("/view")
def view_all_movies():
    data = load_data()
    return data

@app.get("/movies/{movie_id}")
def view_single_movie(movie_id:str):
    data = load_data()
    if movie_id not in data:
        raise HTTPException(status_code = 404 , detail = "Movie Not found")
    return data[movie_id]

@app.post("/movies/add")
def create_movie(movie_id :str,movie:Movie):
    data = load_data()
    if movie_id in data:
        raise HTTPException(status_code = 400 , detail = "Movie already exists")
    
    data[movie_id] = movie.model_dump(exclude = ['id'])
    save_data(data)
    
    return {"message": "Movie added successfully"}

@app.put("/movies/edit/{movie_id}")
def update_info(movie_id: str, movie:UpdateMovie):
    data = load_data()
    if movie_id not in data:
        raise HTTPException(status_code = 404 , detail = "Movie not found")
    
    existing_moive = data[movie_id]

    updating_movie = movie.model_dump(exclude_unset=True)

    for key,value in updating_movie.items():
        existing_moive[key] = value

    existing_moive['id'] = movie_id

    movie_pydantic_obj = Movie(**existing_moive)

    existing_moive = movie_pydantic_obj.model_dump(exclude={"id"})

    data[movie_id] = existing_moive

    save_data(data)
    return JSONResponse(status_code = 200 ,content={'message':'Movie updated'})

@app.delete("/delete/{movie_id}")
def delete_info(movie_id:str):
    data = load_data()
    if movie_id not in data:
        raise HTTPException(status_code = 404 , detail = "Movie not found")
    
    del data[movie_id]

    save_data(data)
    return JSONResponse(status_code = 200 ,content={'message':'Movie Deleted'})