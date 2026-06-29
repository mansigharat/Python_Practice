# code no. 3

import asyncio

async def fetch_weather(city):
    print(f"Fetching the weather of: {city}")
    await asyncio.sleep(2)
    return f"{city}: sunny"

async def main():
    tasks = [
        fetch_weather("Mumbai"),
        fetch_weather("Delhi"),
        fetch_weather("Banglore")
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())