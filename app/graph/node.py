from app.services.analyzed_poem import analyzed_poem
from app.services.compose_poem import compose_poem
from app.services.extract_emotion import extract_emotion
from app.graph.state import PoemState, VideoState
from app.services.extract_context import extract_context

from app.services.extract_tone import extract_tone


async def context_node(state: PoemState):
    video_json = state["video_json"]

    general = video_json.get("general_attributes", {})

    scene = general.get("scene", {})
    human_presence = general.get("human_presence", {})
    emotional_vibe = general.get("emotional_vibe", {})

    context_node = await extract_context(scene, human_presence, emotional_vibe)

    return {
        "core_message": context_node.get("core_message"),
        "moment_description": context_node.get("moment_description"),
        "underlying_theme": context_node.get("underlying_theme"),
        "video_json": video_json
    }


async def emotion_node(state: dict):
    video_json = state.get("video_json", {})
    general = video_json.get("general_attributes", {})

    emotional_vibe = general.get("emotional_vibe", {})
    human_presence = general.get("human_presence", {})

    energy_level = emotional_vibe.get("energy_level", "")
    visible_emotions = human_presence.get("visible_emotions", [])

    core_message = state.get("core_message", "")
    moment_description = state.get("moment_description", "")
    underlying_theme = state.get("underlying_theme")

    emotion_node = await extract_emotion(energy_level, visible_emotions, core_message, moment_description, underlying_theme)

    return {
        "primary_emotion": emotion_node.get("primary_emotion", ""),
        "secondary_emotions": emotion_node.get("secondary_emotions", []),
        "emotional_arc": emotion_node.get("emotional_arc", ""),
        "emotional_intensity": emotion_node.get("emotional_intensity", 0.0)
    }


async def poem_analyzer(state: PoemState):
    core_message = state["core_message"]
    moment_description = state["moment_description"]
    primary_emotion = state["primary_emotion"]
    secondary_emotions = state["secondary_emotions"]

    analyzed = await analyzed_poem(
        core_message, moment_description, primary_emotion, secondary_emotions)

    return {
        "central_theme": analyzed.get("central_theme", ""),
        "mood": analyzed.get("mood", ""),
        "narrative_voice": analyzed.get("narrative_voice", "")
    }


async def tone_node(state: PoemState):
    mood = state["mood"]
    narrative_voice = state["narrative_voice"]

    selected_tone = await extract_tone(mood, narrative_voice)
    return {
        "selected_tone": selected_tone
    }


async def final_composer(state: PoemState):
    core_message = state["core_message"]
    moment_description = state["moment_description"]
    primary_emotion = state["primary_emotion"]
    secondary_emotions = state["secondary_emotions"]
    central_theme = state["central_theme"]
    mood = state["mood"]
    narrative_voice = state["narrative_voice"]
    selected_tone = state["selected_tone"]

    final_poem = await compose_poem(core_message, moment_description, primary_emotion,
                              secondary_emotions, central_theme, mood, narrative_voice, selected_tone)
    
    return {
        "final_poem": final_poem.get("final_poem")
    }
