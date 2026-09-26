from agents import Agent, Runner
from agents.decorators import tool

from deepseek_config import model

# 1. 模拟数据库
# 注意：虚拟数据，不是真实行情
MOCK_DATA = {
    "NVDA": {
        "company": "NVDA",
        "price": 100,
        "eps": 5,
    },
    "AAPL": {
        "company": "AAPL",
        "price": 200,
        "eps": 10,
    }
}


# 定义工具
@tool
def get_stock_info(ticker: str) -> str:
    """根据股票代码查询模拟股价和eps"""
    print(f"[工具执行] get_stock_info:{ticker}")

    ticker = ticker.upper()

    if ticker not in MOCK_DATA:
        return "数据库里没有该公司数据"

    data = MOCK_DATA[ticker]

    return (
        f"公司：{data['company']}\n"
        f"模拟股价：{data['price']}\n"
        f"模拟eps：{data['eps']}\n"
        "数据性质：教学数据"
    )


# 3. 创建agent
agent = Agent(
    name="stock Research agent",
    instructions=(
        "你是一个金融信息助手。"
        "查询公司数据时必须调用工具。"
        "没有数据时不得编造。"
        "必须说明工具数据是虚构的教学数据。"
        "计算市盈率时使用股价除以EPS。"
    ),
    tools=[get_stock_info],
    model=model,
)

# 4. 执行agent
question = "请查询微软的数据并计算市盈率。"
result = Runner.run_sync(
    agent,
    question,
    max_turns=5,
)

# 5. 查看结果
print("\n最终回答：")
print(result.final_output)

print("\n执行记录：")
for item in result.new_items:
    print(item.type)
