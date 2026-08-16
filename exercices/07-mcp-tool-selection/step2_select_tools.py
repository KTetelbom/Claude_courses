import os

import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

# Step 2: disable every tool from the server by default, then re-enable only
# the ones we actually want Claude to use. Adjust ENABLED_TOOLS below to
# match the exact tool names printed by step1_list_tools.py — DeepWiki
# currently exposes "read_wiki_structure", "read_wiki_contents" and
# "ask_question"; here we only keep "ask_question".
ENABLED_TOOLS = ["ask_question"]

response = client.beta.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "What does the anthropics/anthropic-sdk-python repo do?",
        }
    ],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://mcp.deepwiki.com/mcp",
            "name": "deepwiki",
        }
    ],
    tools=[
        {
            "type": "mcp_toolset",
            "mcp_server_name": "deepwiki",
            "default_config": {"enabled": False},
            "configs": {name: {"enabled": True} for name in ENABLED_TOOLS},
        }
    ],
    betas=["mcp-client-2025-11-20"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
    elif block.type == "mcp_tool_use":
        print(f"[tool used: {block.name}]")
