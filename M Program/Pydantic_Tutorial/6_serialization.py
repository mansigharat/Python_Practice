from pydantic import BaseModel

class Address(BaseModel):
    
    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str = 'female'
    age : int
    address : Address

address_dict = { 'city' : 'gurgoan','state':'haryana','pin':'410203'}

address1 = Address(**address_dict)

patient_dict = {
    'name': 'Manasi',
    'gender' : 'female',
    'age': 20,
    'address' : address1
}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude= {'address' : ['state']})
temp = patient1.model_dump(include= {'address' : ['state']})
temp = patient1.model_dump(include= ('name'))
temp = patient1.model_dump(exclude_unset= True)


# temp = patient1.model_dump_json()
print(temp)
print(type(temp))