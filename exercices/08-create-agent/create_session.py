import os

import anthropic
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

# Combines the previous two scripts (main.py + create_environment.py) so a
# session can be created in one run, since it needs a live agent.id and
# environment.id at the same time.
agent = client.beta.agents.create(
    name="Line Counter",
    model="claude-opus-5",
    system="You are a helpful agent that completes small file tasks.",
    tools=[
        {"type": "agent_toolset_20260401", "default_config": {"enabled": True}}
    ],
    betas=["managed-agents-2026-04-01"],
)

environment = client.beta.environments.create(
    name="line-counter-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Count lines demo",
)

print(session.id)  # reference this ID to send the agent a task and stream events
