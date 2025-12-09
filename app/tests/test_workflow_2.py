import asyncio
from app.graph.workflow import graph

async def test_run():
    input_json = {
        "general_attributes": {
            "scene": {
                "setting": "A warm study room",
                "time_of_day": "Late evening",
                "season": "Winter",
                "location_type": "Indoor",
                "natural_elements": ["cool air through window"],
                "objects_in_scene": ["books", "laptop", "mug of coffee", "lamp"]
            },
            "visual": {
                "lighting": "Soft warm desk lamp",
                "color_palette": "Warm yellow, brown, muted blue",
                "camera_style": "Close and intimate",
                "shot_type": "Close-up",
                "movement_in_frame": "Pages turning slowly",
                "visual_textures": ["paper grain", "soft fabric blanket"]
            },
            "audio": {
                "sound_type": "Page flips and light typing",
                "music_genre": "Classical piano",
                "music_mood": "Focused and calm"
            },
            "human_presence": {
                "people_count": 1,
                "social_context": "Studying alone",
                "visible_emotions": ["determination", "slight fatigue"],
                "activities": ["highlighting notes", "typing on laptop"]
            },
            "emotional_vibe": {
                "energy_level": "Medium",
                "overall_mood": "Focused, cozy",
                "aesthetic_vibe": "Warm academic vibe"
            }
        },
        "quote_type_specific": {
            "motivation_and_presence": {
                "sensory_details": ["warm lamp glow", "coffee aroma"],
                "ambiance": "Cozy productivity",
                "action": "Studying intensely",
                "momentum": "Steady push forward",
                "contrast": "Cold weather outside vs warm room inside",
                "focus_point": "Open notebook under lamp",
                "symbolic_elements": ["coffee as drive", "lamp as clarity"]
            },
            "poetry_and_wholesome_reflection": {
                "melodic_elements": "Soft piano rhythm",
                "atmospheric_details": ["steam rising from coffee"],
                "natural_imagery": ["winter wind against window"],
                "micro_movements": ["fingers tapping keys"],
                "textures": ["paper edges", "ceramic mug"],
                "emotional_purity": "A gentle dedication"
            },
            "relatable_comfort": {
                "setting_context": "Winter exam preparation",
                "company_type": "Solo grind",
                "contrasting_activity": "Fighting sleepiness",
                "state_of_mind": "Focused but tired",
                "fatigue_signs": "Yawns, slow blinking",
                "comfort_cues": ["warm blanket", "hot drink"]
            },
            "nostalgia_and_memory": {
                "sensory_triggers": ["smell of old books"],
                "visual_cues": ["lamp glow on desk"],
                "time_markers": "Late-night winter study sessions",
                "nostalgic_vibe": "Reminds of school exam days",
                "repetitive_actions": ["night studying"],
                "emotional_residue": "Warm determination"
            }
        },
        "metadata_tags": ["study", "cozy room", "winter", "focus", "student"]
    }


    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
