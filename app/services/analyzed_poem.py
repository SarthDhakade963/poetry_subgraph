import asyncio
import json
from typing import List
import google.generativeai as genai

from app.llm._generate import _generate
from app.prompt.poem_analyzer_node_prompt import POEM_ANALYZER_PROMPT


async def analyzed_poem(core_message: str, moment_description: str, primary_emotion: str, secondary_emotions: List[str]):
    """
    Calls Gemini LLM to analyze poem and extract central_theme, mood, and narrative_voice.
    """

    prompt = POEM_ANALYZER_PROMPT.format(
        core_message=core_message or "",
        moment_description=moment_description or "",
        primary_emotion=primary_emotion or "",
        secondary_emotions=json.dumps(secondary_emotions or [])
    )

    raw = await asyncio.to_thread(_generate, prompt)

    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "central_theme": "",
            "mood": "",
            "narrative_voice": ""
        }
