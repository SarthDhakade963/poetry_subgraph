from textwrap import dedent

COMPOSE_POEM_PROMPT = dedent("""
You are a master poet. Use ONLY the input data. Do NOT hallucinate or invent details.

INPUT DATA:
core_message: {core_message}
moment_description: {moment_description}
primary_emotion: {primary_emotion}
secondary_emotions: {secondary_emotions}
central_theme: {central_theme}
mood: {mood}
narrative_voice: {narrative_voice}
selected_tone: {selected_tone}

Compose a polished, lyrical poem that:
- Reflects the emotions (primary and secondary) precisely.
- Embeds the imagery from core_message and moment_description.
- Matches the central_theme, mood, narrative_voice, and selected_tone.
- Uses poetic devices (metaphors, symbolism) where appropriate.
- Has natural flow, stanza breaks, and cadence.
- Feels cinematic and immersive, yet human and shareable.

Return JSON ONLY with the field:
- final_poem (string)
""").strip()
