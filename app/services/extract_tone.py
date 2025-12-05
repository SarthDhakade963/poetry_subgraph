import asyncio
import json
import google.generativeai as genai

from app.llm._generate import _generate
from app.prompt.tone_node_prompt import TONE_NODE_PROMPT


async def extract_tone(mood: str, narrative_voice: str):
    """
    Calls Gemini LLM to determine the poem's cinematic/poetic tone.
    """

    prompt = TONE_NODE_PROMPT.format(
        mood=mood or "",
        narrative_voice=narrative_voice or ""
    )

    raw = await asyncio.to_thread(_generate, prompt)
    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "selected_tone": "neutral"
        }
