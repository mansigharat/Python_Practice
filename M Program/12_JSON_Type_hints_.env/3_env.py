from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL_NAME")

print(api_key)   # sk-abc123yoursecretkey
print(model)     # gpt-4

# .env         = file storing secrets
# load_dotenv() = loads .env into memory
# os.getenv()  = reads the value
# .gitignore   = tells git to ignore .env file