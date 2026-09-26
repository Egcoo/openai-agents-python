from agents import Agent, Runner, RunConfig

from deepseek_config import model

finance_agent = Agent(
    name="Finance Agent",
    handoff_description="处理财务、估值、市盈率等问题。",
    instructions=(
        "你是一名财务分析助手。"
        "只负责财务和估值相关问题。"
    ),
)

news_agent = Agent(
    name="News Agent",
    handoff_description="处理公司新闻、事件和市场动态问题。",
    instructions=(
        "你是一名公司新闻分析助手。"
        "只负责新闻和事件相关问题。"
    ),
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "判断用户问题属于财务分析还是新闻分析，"
        "并把任务交给合适的专业 Agent。"
    ),
    handoffs=[
        finance_agent,
        news_agent,
    ],

)

result = Runner.run_sync(
    triage_agent,
    "请分析一家公司的财务情况",
    run_config=RunConfig(
        model=model,
        tracing_disabled=True,
    ),
)

print(result.final_output)
print("最终 Agent:", result.last_agent.name)
