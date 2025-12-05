import asyncio
from app.graph.workflow import graph

async def test_run():
    input_json = {
        "scene": {
            "setting": "city park",
            "time_of_day": "late afternoon",
            "season": "spring",
            "natural_elements": ["green grass", "cherry blossoms", "gentle breeze"],
            "objects_in_scene": ["park bench", "fountain", "lamp posts"],
        },

        "human_presence": {
            "people_count": 2,
            "social_context": "man observing girl from a distance",
            "activities": ["man standing quietly", "girl walking or playing"],
            "visible_emotions": ["man: curious", "girl: joyful"],
        },

        "emotional_vibe": {
            "overall_mood": "contemplative",
            "energy_level": "mild and thoughtful",
        },
    }

    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
