import os

import anthropic
from anthropic.lib import files_from_dir
from dotenv import load_dotenv

# Load ANTHROPIC_API_KEY from .env.local at the repo root, regardless of
# where this script is run from.
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

SKILL_DIR = os.path.join(
    os.path.dirname(__file__), "..", "04-skills-status-report", "status-report-generator"
)
SKILL_DISPLAY_TITLE = "Status Report Generator"


def get_or_create_skill():
    # Reuse the skill from exercise 4 if it already exists, instead of
    # creating a fresh duplicate every time this script runs.
    existing = client.beta.skills.list(betas=["skills-2025-10-02"])
    for s in existing.data:
        if s.display_title == SKILL_DISPLAY_TITLE:
            return s

    return client.beta.skills.create(
        display_title=SKILL_DISPLAY_TITLE,
        files=files_from_dir(SKILL_DIR),
        betas=["skills-2025-10-02"],
    )


skill = get_or_create_skill()

activity_log = """
09:12 - Deployed the auth service migration to staging (3/5 services done)
10:40 - Blocked on the payments API: waiting for updated credentials from vendor
11:15 - Reviewed 4 PRs for the onboarding flow
14:00 - Started writing tests for the new billing webhook
16:30 - Planning tomorrow: finish billing tests, retry payments API once creds arrive
"""

response = client.beta.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    betas=["skills-2025-10-02", "code-execution-2025-08-25"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": skill.id,
                "version": "latest",
            }
        ]
    },
    tools=[
        {
            "type": "code_execution_20250825",
            "name": "code_execution",
        }
    ],
    messages=[
        {
            "role": "user",
            "content": f"Generate the daily status report from this activity log:\n\n{activity_log}",
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
