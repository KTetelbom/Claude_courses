import os

import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

# Step 1: connect to the DeepWiki MCP server with every tool it exposes
# enabled (the default), and ask Claude to enumerate them with their exact
# names. Use those exact names in step 2 to enable only a subset.
response = client.beta.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "List every tool you have available from the deepwiki MCP server. "
            "For each one, give its exact tool name and a one-line description.",
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
        }
    ],
    betas=["mcp-client-2025-11-20"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
