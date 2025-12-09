import asyncio
from app.graph.workflow import graph


async def test_run():
    input_json = {
        "general_attributes": {
            "scene": {
                "setting": "A quiet street corner in the rain",
                "time_of_day": "Night",
                "season": "Monsoon",
                "location_type": "Urban outdoor",
                "natural_elements": ["rain droplets", "wet asphalt", "misty air"],
                "objects_in_scene": ["streetlight", "umbrella", "puddle reflections"]
            },
            "visual": {
                "lighting": "Soft yellow streetlight glow",
                "color_palette": "Deep blue, grey, warm yellow",
                "camera_style": "Moody, slow-motion",
                "shot_type": "Medium shot",
                "movement_in_frame": "Raindrops falling continuously",
                "visual_textures": ["wet ground shimmer", "misty air", "fabric of umbrella"]
            },
            "audio": {
                "sound_type": "Rainfall and distant traffic",
                "music_genre": "Lo-fi",
                "music_mood": "Melancholic but warm"
            },
            "human_presence": {
                "people_count": 1,
                "social_context": "Waiting alone",
                "visible_emotions": ["patience", "soft sadness"],
                "activities": ["holding an umbrella", "looking at the road"]
            },
            "emotional_vibe": {
                "energy_level": "Low",
                "overall_mood": "Quiet and introspective",
                "aesthetic_vibe": "Cinematic rainy-night aesthetic"
            }
        },
        "quote_type_specific": {
            "motivation_and_presence": {
                "sensory_details": ["cold droplets", "streetlight warmth"],
                "ambiance": "Stillness mixed with rain's rhythm",
                "action": "Waiting quietly",
                "momentum": "Slow, steady",
                "contrast": "Warm yellow light against cold blue rain",
                "focus_point": "Umbrella lit by the streetlight",
                "symbolic_elements": ["rain as cleansing", "light as hope"]
            },
            "poetry_and_wholesome_reflection": {
                "melodic_elements": "Soft patter of rain",
                "atmospheric_details": ["foggy breath", "shimmering reflections"],
                "natural_imagery": ["silver rain threads", "glowing puddles"],
                "micro_movements": ["umbrella shaking slightly"],
                "textures": ["wet asphalt", "fabric ripples"],
                "emotional_purity": "A simple longing"
            },
            "relatable_comfort": {
                "setting_context": "Returning home late",
                "company_type": "None",
                "contrasting_activity": "Waiting after a tiring day",
                "state_of_mind": "Emotionally drained but steady",
                "fatigue_signs": "Drooping shoulders",
                "comfort_cues": ["streetlight warmth", "steady rain"]
            },
            "nostalgia_and_memory": {
                "sensory_triggers": ["smell of rain", "streetlight warmth"],
                "visual_cues": ["reflection in puddles"],
                "time_markers": "Late night monsoon",
                "nostalgic_vibe": "Reminds of old walks home",
                "repetitive_actions": ["waiting in the rain"],
                "emotional_residue": "Bittersweet warmth"
            }
        },
        "metadata_tags": ["rain", "streetlight", "girl", "night", "nostalgia"]
    }


    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
