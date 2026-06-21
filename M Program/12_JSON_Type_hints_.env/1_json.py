import json

# json.loads()  = JSON string  -> Python dict  (string IN)
# json.dumps()  = Python dict  -> JSON string  (string OUT)
# json.load()   = JSON file    -> Python dict  (file IN)
# json.dump()   = Python dict  -> JSON file    (file OUT)

people_String = '''
{
    "people": [
        {
            "name": "Mansi Gharat",
            "phone" : "9876543210",
            "emails" : ["mansigharat@gmail.com" , "mansigharat2@gmail.com"],
            "has_license" : false
        },
        {
        "name": "Parth Gharat",
        "phone" : "9876501236",
        "emails" : ["parthgharat@gmail.com" , "parthgharat2@gmail.com"],
        "has_license" : true
        }
    ]
}
'''

data = json.loads(people_String)
print(type(data))

# JSON string to Python dict

json_string = '{"name": "Rahul", "age": 25}'
data = json.loads(json_string)
print(data["name"])  # Rahul


response = '{"model": "claude-3", "tokens": 150, "status": "success"}'
data = json.loads(response)
print(data["model"])

response = '{"agent": "ResearchAgent", "result": {"topic": "AI trends", "sources": 5, "summary": "AI is growing fast"}, "status": "success"}'
data = json.loads(response)
print(data["result"]["summary"])
