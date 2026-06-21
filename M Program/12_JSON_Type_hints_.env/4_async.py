# import asyncio

# async def call_api(name, seconds):
#     print(f"{name} started")
#     await asyncio.sleep(seconds)  # simulating API wait
#     print(f"{name} done")
#     return f"{name} result"

# async def main():
#     # without async - one by one - 9 seconds total
#     # with async - all at once - 3 seconds total
#     results = await asyncio.gather(
#         call_api("ResearchAgent", 3),
#         call_api("WriterAgent", 3),
#         call_api("CoderAgent", 3),
#     )
#     print(results)

# asyncio.run(main())

# # import time

# # def call_api(name, seconds):
# #     print(f"{name} started")
# #     time.sleep(seconds)
# #     print(f"{name} done")
# #     return f"{name} result"

# # def main():
# #     results = []
# #     results.append(call_api("ResearchAgent", 3))
# #     results.append(call_api("WriterAgent", 5))
# #     results.append(call_api("CoderAgent", 7))
# #     print(results)

# # main()

import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="your-key")

async def research_agent(topic):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Research {topic}"}]
    )
    return response.choices[0].message.content

async def writer_agent(content):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write summary: {content}"}]
    )
    return response.choices[0].message.content

async def main():
    results = await asyncio.gather(
        research_agent("AI trends"),
        writer_agent("machine learning"),
    )
    print(results)

asyncio.run(main())