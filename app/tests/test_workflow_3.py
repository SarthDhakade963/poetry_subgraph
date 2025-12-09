import asyncio
from app.graph.workflow import graph


async def test_run():
    input_json = {
        "general_attributes": {
            "scene": {
                "setting": "A misty forest trail",
                "time_of_day": "Early morning",
                "season": "Spring",
                "location_type": "Nature trail",
                "natural_elements": ["low fog", "dew on leaves", "soft morning light", "birds chirping"],
                "objects_in_scene": ["muddy path", "fallen branches", "backpack straps"]
            },
            "visual": {
                "lighting": "Diffused soft light through fog",
                "color_palette": "Muted green, pale grey, earthy brown",
                "camera_style": "Slow-moving handheld",
                "shot_type": "Medium-follow shot",
                "movement_in_frame": "Fog drifting subtly",
                "visual_textures": ["wet leaves", "rough bark", "misty air"]
            },
            "audio": {
                "sound_type": "Distant birds and crunching footsteps",
                "music_genre": "Ambient nature pads",
                "music_mood": "Calm and awakening"
            },
            "human_presence": {
                "people_count": 1,
                "social_context": "Solo morning walk",
                "visible_emotions": ["peaceful", "clear-headed"],
                "activities": ["walking slowly", "observing surroundings"]
            },
            "emotional_vibe": {
                "energy_level": "Low to medium",
                "overall_mood": "Calm and rejuvenating",
                "aesthetic_vibe": "Misty, natural, introspective"
            }
        },
        "quote_type_specific": {
            "motivation_and_presence": {
                "sensory_details": ["cool mist", "fresh earthy scent", "soft light"],
                "ambiance": "Quiet and awakening",
                "action": "Walking through fog-covered path",
                "momentum": "Slow but purposeful",
                "contrast": "Brightening sky against dark trunks",
                "focus_point": "Silhouette moving deeper into the forest",
                "symbolic_elements": ["fog as uncertainty", "path as journey forward"]
            },
            "poetry_and_wholesome_reflection": {
                "melodic_elements": "Soft layered nature sounds",
                "atmospheric_details": ["floating fog", "morning stillness"],
                "natural_imagery": ["silver mist", "emerald leaves"],
                "micro_movements": ["droplets falling", "fog shifting"],
                "textures": ["rough bark", "wet earth"],
                "emotional_purity": "A quiet restart to the day"
            },
            "relatable_comfort": {
                "setting_context": "Early-morning walk to clear the mind",
                "company_type": "Solo self-care",
                "contrasting_activity": "Taking a break from screens/work",
                "state_of_mind": "Calm clarity",
                "fatigue_signs": "Soft yawns, gentle breathing",
                "comfort_cues": ["cool air", "soothing silence"]
            },
            "nostalgia_and_memory": {
                "sensory_triggers": ["smell of wet soil", "sound of birds"],
                "visual_cues": ["fog hugging tree trunks"],
                "time_markers": "Early spring mornings",
                "nostalgic_vibe": "Feels like old hiking days",
                "repetitive_actions": ["morning forest walks"],
                "emotional_residue": "Lingering calm and renewal"
            }
        },
        "metadata_tags": ["forest", "fog", "morning", "nature walk", "calm"]
    }


    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
