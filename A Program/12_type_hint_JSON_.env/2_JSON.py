# import json

# person = {
#     "name": "Chocolate",
#     "age": 21,
#     "skills": ["Python", "AI"]
# }

# # dict to string
# json_string = json.dumps(person)
# print(type(json_string))
# print(json_string)

# # string back to dict
# back_to_dict = json.loads(json_string)
# print(type(back_to_dict))
# print(back_to_dict["name"])



# job = {
#     "name": "Atharva Thorve",
#     "age": "20",
#     "mob number" : "9108910899",

# }

# import json

# person = {"name": "Chocolate", "age": 21}

# json_string = json.dumps(person)

# print(json_string["name"])  # this will crash. why?




  
# 3rd code

# import json
# from pathlib import Path

# data = {
#     "agent" : "sales_bot",
#     "last _action" : "sent_email",
#     "success" : True
# }

# file = Path ("agent_log.json")

# with file.open("w") as f:
#     json.dump(data, f, indent=2)

# with file.open("r") as f:
#     loaded = json.load(f)


# print(loaded["agent"])
# print(loaded["success"])


import json

weather = {
    "city": "Mumbai",
    "temperature": 34,
    "is_raining": False,
    "forecast": ["sunny", "cloudy", "rain"]
}

# Write the dictionary to a JSON file
with open("weather.json", "w") as f:
    json.dump(weather, f)

# Read the JSON file back into a dictionary
with open("weather.json", "r") as f:
    weather = json.load(f)

# Print the city and the first forecast
print(weather["city"])
print(weather["forecast"][0])