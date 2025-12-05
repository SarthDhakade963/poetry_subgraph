import asyncio
import json
import google.generativeai as genai

from app.llm._generate import _generate
from app.prompt.poem_composer_prompt import COMPOSE_POEM_PROMPT


async def compose_poem(core_message: str,
                       moment_description: str,
                       primary_emotion: str,
                       secondary_emotions: list,
                       central_theme: str,
                       mood: str,
                       narrative_voice: str,
                       selected_tone: str):
    """
    Calls Gemini LLM to generate the final poem based on all inputs.
    """

    prompt = COMPOSE_POEM_PROMPT.format(
        core_message=core_message or "",
        moment_description=moment_description or "",
        primary_emotion=primary_emotion or "",
        secondary_emotions=json.dumps(secondary_emotions or []),
        central_theme=central_theme or "",
        mood=mood or "",
        narrative_voice=narrative_voice or "",
        selected_tone=selected_tone or ""
    )

    raw = await asyncio.to_thread(_generate,prompt)
    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "final_poem": ""
        }
