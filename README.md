# todo-example-app

A tutorial example demonstrating how to build and deploy an MCP agent using mcp-agent. This simple todo assistant helps you manage your tasks through natural language interactions.

## About mcp-agent

mcp-agent is a simple, composable framework to build agents using Model Context Protocol.

**Inspiration:** Anthropic announced 2 foundational updates for AI application developers:

- **Model Context Protocol** - a standardized interface to let any software be accessible to AI assistants via MCP servers.
- **Building Effective Agents** - a seminal writeup on simple, composable patterns for building production-ready AI agents.

mcp-agent puts these two foundational pieces into an AI application framework:

- It handles the pesky business of managing the lifecycle of MCP server connections so you don't have to.
- It implements every pattern described in Building Effective Agents, and does so in a composable way, allowing you to chain these patterns together.
- **Bonus:** It implements OpenAI's Swarm pattern for multi-agent orchestration, but in a model-agnostic way.

Altogether, this is the simplest and easiest way to build robust agent applications. Much like MCP, this project is in early development.

## Setup Instructions

Prerequisites:
- Python 3.10+
- uv

1. Initialize a new UV project:
```bash
uv init
```

2. Add the mcp-agent dependency:
```bash
uv add mcp-agent
```

3. Add the OpenAI dependency:
```bash
uv add openai
```

4. Configure your OpenAI API key in `mcp_agent.secrets.yaml`

## Usage

### Run Locally
```bash
uv run main.py
```

### Deploy to the Cloud
```bash
uv run mcp-agent deploy --no-auth
```

## Connect to Chat

### ChatGPT

Add custom connector

**example url**: `https://1m82g32x8nkoppinayx0k5ye12oar6vk.deployments.mcp-agent.com/sse`

https://github.com/user-attachments/assets/cb50700c-5650-4f12-ac2e-2eabba5c8144

### Claude Desktop

Add custom connector

**example url**: `https://1m82g32x8nkoppinayx0k5ye12oar6vk.deployments.mcp-agent.com/sse`

<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/e9367309-7ebd-4e40-aa16-56dcae17b5eb" />
