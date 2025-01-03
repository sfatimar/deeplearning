from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent (
        name="Web Agent",
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[GoogleSearch()],
        instructions=["Given a topic by the user, respond with 4 latest news items about that topic."],
        show_tool_calls=True,
        markdown=True
)

finance_agent = Agent (
        name="Finance Agent",
        role="Get Financial Data", 
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
        instructions=["use tables to display data"],
        show_tool_calls=True,
        markdown=True
 )

agent_team = Agent (
        team=[web_agent, finance_agent],
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=["use tables to display data"],
        show_tool_calls=True,
        markdown=True
)

agent_team.print_response("summarize analyst recommendations and latest news for INTC")

