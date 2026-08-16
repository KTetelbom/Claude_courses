import os

import anthropic
from dotenv import load_dotenv

# Load ANTHROPIC_API_KEY from .env.local at the repo root, regardless of
# where this script is run from.
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

# DeepWiki's MCP server is public and requires no authorization_token,
# unlike Linear's — handy to test the mcp_servers/mcp_toolset mechanics
# without needing an account anywhere.
response = client.beta.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "What tools do you have available, and what does the anthropics/anthropic-sdk-python repo do?",
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
