# async marks a function as one that can do smart waiting. You put it before def.
# await is used inside an async function to say "start this task and come back when it is ready, do not just stand there.


#code no. 1

# import asyncio

# async def fetch_weather(city):
#     print(f"Fetching weather for {city}")
#     await asyncio.sleep(2)  # simulates API wait time
#     print(f"Got weather for {city}")
#     return f"{city}: 34 degrees"

# async def main():
#     result = await fetch_weather("Mumbai")
#     print(result)

# asyncio.run(main())


# code 2

import asyncio

async def fetch_weather(city):
    print(f"Fetching {city}")
    await asyncio.sleep(2)
    return f"{city}: 34 degrees"

async def main():
    tasks = [
        fetch_weather("Mumbai"),
        fetch_weather("Delhi"),
        fetch_weather("Pune")
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())