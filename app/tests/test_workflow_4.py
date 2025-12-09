import asyncio
from app.graph.workflow import graph


async def test_run():
    input_json = {
        "general_attributes": {
            "scene": {
                "setting": "A peaceful beach shoreline",
                "time_of_day": "Sunset",
                "season": "Late summer",
                "location_type": "Coastal outdoor setting",
                "natural_elements": ["soft waves", "orange sky", "warm breeze", "glowing horizon"],
                "objects_in_scene": ["sand", "driftwood", "a backpack", "footprints"]
            },
            "visual": {
                "lighting": "Golden-hour warm lighting",
                "color_palette": "Orange, gold, soft blue, sand beige",
                "camera_style": "Cinematic, slow-pan",
                "shot_type": "Wide shot",
                "movement_in_frame": "Gentle waves rolling in",
                "visual_textures": ["grainy sand", "shimmering water", "soft sky gradients"]
            },
            "audio": {
                "sound_type": "Soft waves crashing",
                "music_genre": "Ambient acoustic",
                "music_mood": "Warm and reflective"
            },
            "human_presence": {
                "people_count": 1,
                "social_context": "Alone, peaceful solitude",
                "visible_emotions": ["calm", "content", "reflective"],
                "activities": ["sitting on the sand", "watching the sunset"]
            },
            "emotional_vibe": {
                "energy_level": "Low and soothing",
                "overall_mood": "Serene and reflective",
                "aesthetic_vibe": "Warm, cinematic, peaceful"
            }
        },
        "quote_type_specific": {
            "motivation_and_presence": {
                "sensory_details": ["warm breeze", "sound of waves", "golden light"],
                "ambiance": "Calm but inspiring",
                "action": "Watching the sun sink slowly",
                "momentum": "A gentle sense of renewal",
                "contrast": "Warm sky against cool waves",
                "focus_point": "The fading sun over the ocean",
                "symbolic_elements": ["sunset symbolizing closure", "waves symbolizing consistency"]
            },
            "poetry_and_wholesome_reflection": {
                "melodic_elements": "Soft, flowing rhythm like ocean tides",
                "atmospheric_details": ["glowing sky", "slow-moving clouds"],
                "natural_imagery": ["melting sun", "whispering waves"],
                "micro_movements": ["shimmer on water", "brush of breeze"],
                "textures": ["grains of sand", "smooth water surface"],
                "emotional_purity": "Quiet gratitude for the moment"
            },
            "relatable_comfort": {
                "setting_context": "A long day ending by the shore",
                "company_type": "Solo comfort",
                "contrasting_activity": "Resting after mental exhaustion",
                "state_of_mind": "Unwinding and breathing freely",
                "fatigue_signs": "Relaxed shoulders, slow breathing",
                "comfort_cues": ["warm colors", "soft sounds", "open horizon"]
            },
            "nostalgia_and_memory": {
                "sensory_triggers": ["smell of ocean air", "glow of dusk"],
                "visual_cues": ["silhouette against sunset"],
                "time_markers": "End of day, summer evening",
                "nostalgic_vibe": "Reminds of childhood vacations",
                "repetitive_actions": ["coming to the beach at sunset"],
                "emotional_residue": "A quiet feeling of belonging"
            }
        },
        "metadata_tags": ["beach", "sunset", "calm", "solo", "warm"]
    }

    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
