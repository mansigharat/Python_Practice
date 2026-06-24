from pydantic import BaseModel
from typing import List,Dict

class Patient(BaseModel):

    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('Update')

patient_info = {'name' : 'Manasi' , 'age' : "20",'weight' : 40.9 ,'married': False,'allergies':['pollen','dust'] , 'contact_details' : {'email' : 'mansigharat@gmail.com' , 'Phone_number' : '9876543210'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
