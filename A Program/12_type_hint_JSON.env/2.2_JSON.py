# use of type dict, type hints, nested types, in JSON.

import json
from pathlib import Path
from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


class Memory(TypedDict):
    session_id: str
    user_name: str
    messages: list[Message]


memory: Memory = {
    "session_id": "choco123",
    "user_name": "Chocolate",
    "messages": [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thanks for asking!"},
    ],
}

path = Path("memory.json")

with open(path, "w") as f:
    json.dump(memory, f, indent=2)

with open(path, "r") as f:
    data: Memory = json.load(f)

print(data["messages"][1]["content"])