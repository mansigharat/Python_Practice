

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
city = os.getenv("CITY")

print("API_KEY:", api_key)
print("CITY:", city)


#the os.getenv() is like a command to to computer to get the value of required variable.
# .env         = file storing secrets
# load_dotenv() = loads .env into memory
# os.getenv()  = reads the value
# .gitignore   = tells git to ignore .env file