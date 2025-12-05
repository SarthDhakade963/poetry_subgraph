import asyncio
from app.graph.workflow import graph


async def test_run():
    input_json = {
        "scene": {
            "setting": "beach",
            "time_of_day": "sunset",
            "season": "summer",
            "natural_elements": ["ocean waves", "golden sky", "soft breeze"],
            "objects_in_scene": ["wooden bench", "sand", "distant boats"],
        },

        "human_presence": {
            "people_count": 1,
            "social_context": "solo relaxation",
            "activities": ["sitting", "watching the sunset", "thinking quietly"],
            "visible_emotions": ["peaceful", "calm", "reflective"],
        },

        "emotional_vibe": {
            "overall_mood": "serene",
            "energy_level": "low and soothing",
        },
    }

    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
