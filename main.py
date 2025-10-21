import asyncio
from typing import Optional

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.core.context import Context as AppContext
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

# Create the MCPApp, the root of mcp-agent.
app = MCPApp(name="ToDos", description="Getting started with a To Do app")

@app.tool
async def todo_assistant(request: str, app_ctx: Optional[AppContext] = None) -> str:
    """
    Run an Agent with access to MCP servers (filesystem) to handle 
    the input request.
    """
    agent = Agent(
        name="finder",
        instruction=(
            """You are a helpful assistant. Write and reads my todo's from a todo.md file. The markdown file with the todo's should be well organized and just the checklist of todo's with sub-lists."""
        ),
        server_names=["filesystem"],
        context=app_ctx,
    )

    async with agent:
        llm = await agent.attach_llm(OpenAIAugmentedLLM)
        result = await llm.generate_str(message=request)
        return result

async def main():
    async with app.run() as agent_app:
        # Run the agent
        response = await todo_assistant(
            request="Add milk, bread, and cereal to my grocery list",
            app_ctx=agent_app.context,
        )
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
