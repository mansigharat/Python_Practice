from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name : Annotated[str,Field(max_length = 50,title = "Name of patient",description = 'Give the name of the patient in less than 50 chars',examples=['Manasi','Parth'])]
    age : int= Field(gt=0,lt=120)
    email: EmailStr
    linkedin_url : AnyUrl
    weight : Annotated[float, Field(gt=0,strict=True)]
    married : Annotated[bool,Field(default=None,description="Patient married or not")]
    allergies : Optional[List[str]] = Field(max_length=5)
    contact_details : Dict[str,str]

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient : Patient):

    print(patient.name)
    print(patient.email)
    print('Update')

patient_info = {'name' : 'Manasi' , 'age' : "20", "email" : "abc@gmail.com",'linkedin_url':"http://linkedin.com/11223",'weight' : 40.9 ,'allergies':['pollen','dust'] , 'contact_details' : {'Phone_number' : '9876543210'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
