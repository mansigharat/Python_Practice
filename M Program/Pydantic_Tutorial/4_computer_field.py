from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    weight: float
    height: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print("BMI:", patient.bmi)
    print('Updated')


patient_info = {
    'name': 'Manasi',
    'age': 65,
    'email': 'abc@hdfc.com',
    'weight': 40.9,
    'height': 1.5,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'Phone_number': '9876543210',
        'emergency': '8421593578'
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)