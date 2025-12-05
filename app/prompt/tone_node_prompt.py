from textwrap import dedent

TONE_NODE_PROMPT = dedent("""
You are a Tone Selector. Use ONLY the information provided. Do NOT hallucinate.

INPUT DATA:
mood: {mood}
narrative_voice: {narrative_voice}

Select the most suitable poetic or cinematic tone for this poem. 
Examples of tones: deep cinematic, tender nostalgia, serene reflection, raw honesty, minimalist.

Return JSON ONLY with the field:
- selected_tone (string, one of the suitable tones or descriptive phrase based on input)

If input is missing or unclear, return a neutral or minimal tone.
""").strip()
