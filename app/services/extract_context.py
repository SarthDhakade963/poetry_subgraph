import asyncio
import json

from app.llm._generate import _generate
from app.prompt import CONTEXT_NODE_PROMPT


async def extract_context(scene: dict, human_presence: dict, emotional_vibe: dict):
    """
    Calls Gemini LLM to extract core_message, moment_description, and underlying_theme
    using explicit scene, human presence, and emotional vibe data.
    """

    prompt = CONTEXT_NODE_PROMPT.format(
        scene=json.dumps(scene, indent=2),
        human_presence=json.dumps(human_presence, indent=2),
        emotional_vibe=json.dumps(emotional_vibe, indent=2)
    )

    raw = await asyncio.to_thread(_generate, prompt)

    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "core_message": "",
            "moment_description": "",
            "underlying_theme": ""
        }
