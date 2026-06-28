from fastapi import FastAPI, Path, HTTPException, Query
import json
from pydantic import BaseModel,Field
from typing import Annotated

app = FastAPI()

class Patient(BaseModel):

    id  : Annotated[str,Field(...,description = 'ID of the patient' , examples=['P1001'])]
    name : Annotated[str,Field(...,description = 'Name of the patientp')]
    city: str
    age :Annotated
    gender : str
    height : float
    weight : float

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {
        "message": "A fully functional API to manage your patient records"
    }


@app.get("/view")
def view():
    data = load_data()
    return data


# Path Parameter
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="ID of the patient in the database",
        examples=["P001"]
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# Query Parameter
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight, or BMI"
    ),
    order: str = Query(
        "asc",
        description="Sort order: asc or desc"
    )
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Select either 'asc' or 'desc'"
        )

    data = load_data()

    sort_order = (order == "desc")

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data