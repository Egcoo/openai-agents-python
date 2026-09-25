import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled,
)

load_dotenv()

client = AsyncOpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url=os.environ["DEEPSEEK_BASE_URL"],
)

model = OpenAIChatCompletionsModel(
    model=os.getenv("DEEPSEEK_MODEL", "deepseek-flash"),
    openai_client=client,
)

set_tracing_disabled(True)


async def main():
    agent = Agent(
        name="DeepSeek Assistant",
        instructions="你是一名耐心的中文助手。",
        model=model,
    )

    result = await Runner.run(agent, "用简单的话解释什么是 Agent。")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())