from agents import Agent, Runner, RunConfig
from deepseek_config import model

financial_agent = Agent(
    name="Financial Analyst",
    instructions=(
        "你负责分析公司财务、盈利和估值问题。"
        "返回简洁的专业分析。"
    ),
)

news_agent = Agent(
    name="News Analyst",
    instructions=(
        "你负责分析公司新闻和事件。"
        "返回简洁的专业分析。"
    ),
)

manager_agent = Agent(
    name="Research Manager",

    instructions=(
        "你负责回答用户的公司研究问题。"
        "需要财务分析时调用 financial_analysis。"
        "需要新闻分析时调用 news_analysis。"
        "如果问题同时涉及两方面，可以分别调用。"
        "最后由你综合结果回答用户。"
    ),

    tools=[
        financial_agent.as_tool(
            tool_name="financial_analysis",
            tool_description="分析公司的财务、盈利和估值问题。",
        ),

        news_agent.as_tool(
            tool_name="news_analysis",
            tool_description="分析公司的新闻、事件和市场动态。",
        ),
    ],
)

result = Runner.run_sync(
    manager_agent,
    "请分析APPLE公司的财务情况",
    run_config=RunConfig(
        model=model,
        tracing_disabled=False,
        trace_include_sensitive_data=True
    ),
)

print(result.final_output)
