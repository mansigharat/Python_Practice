from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = str(value).split('@')[1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print('Updated')

patient_info = {
    'name': 'Manasi',
    'age': '20',
    'email': 'abc@hdfc.com',
    'weight': 40.9,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'Phone_number': '9876543210'
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)