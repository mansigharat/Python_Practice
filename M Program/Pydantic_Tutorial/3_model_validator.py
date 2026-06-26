from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


class Patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool = False
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(self):

        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError(
                'Patients older than 60 must have an emergency contact'
            )

        return self


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
    'age': 65,  
    'email': 'abc@hdfc.com',
    'weight': 40.9,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'Phone_number': '9876543210',
        'emergency': '8421593578'
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)