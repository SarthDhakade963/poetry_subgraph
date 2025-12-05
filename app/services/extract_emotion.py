import asyncio
import json

from app.llm._generate import _generate
from app.prompt.emotion_node_prompt import EMOTION_NODE_PROMPT


async def extract_emotion(energy_level, visible_emotions, core_message, moment_description, underlying_theme):
    """
    Calls Gemini LLM to extract emotions based on video JSON + context.
    """

    prompt = EMOTION_NODE_PROMPT.format(
        energy_level=energy_level or "",
        visible_emotions=visible_emotions or [],
        core_message=core_message or "",
        moment_description=moment_description or "",
        underlying_theme= underlying_theme or ""
    )

    raw = await asyncio.to_thread(_generate,prompt)

    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "primary_emotion": "",
            "secondary_emotions": [],
            "emotional_arc": "",
            "emotional_intensity": 0.0
        }
