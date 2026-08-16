import os

import anthropic
from anthropic.lib import files_from_dir
from dotenv import load_dotenv

# Load ANTHROPIC_API_KEY from .env.local at the repo root, regardless of
# where this script is run from.
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env.local"))

client = anthropic.Anthropic()

skill_dir = os.path.join(os.path.dirname(__file__), "status-report-skill")

skill = client.beta.skills.create(
    display_title="Status Report Generator",
    files=files_from_dir(skill_dir),  # folder containing SKILL.md
    betas=["skills-2025-10-02"],
)

print(skill.id)  # reference this ID in future requests
