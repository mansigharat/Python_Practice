# def get_user_info (name: str, age:int, email:str | None = None) -> dict[str, str | int]:
#     return {
#         "name": name,
#         "age": age,
#         "email": email if email else "not provided"
#     }

# result = get_user_info("Atharva", "twenty")
# print(result)


from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str | None = None

u = User(name="Atharva", age=19)
print(u)
print(u.name)
print(u.age)

