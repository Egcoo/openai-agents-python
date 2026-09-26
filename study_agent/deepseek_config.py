import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from agents import OpenAIChatCompletionsModel

load_dotenv()

client = AsyncOpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url=os.environ["DEEPSEEK_BASE_URL"],
)

model = OpenAIChatCompletionsModel(
    model=os.getenv("DEEPSEEK_MODEL", "deepseek-flash"),
    openai_client=client,
)
