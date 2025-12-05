import asyncio
from app.graph.workflow import graph


async def test_run():
    input_json = {
        "scene": {
            "setting": "quiet park",
            "time_of_day": "morning",
            "season": "autumn",
            "natural_elements": ["falling leaves", "soft sunlight", "cool breeze"],
            "objects_in_scene": ["wooden bench", "walking path", "flower beds"],
        },

        "human_presence": {
            "people_count": 2,
            "social_context": "old couple spending time together",
            "activities": ["sitting on the bench", "holding hands", "watching the park"],
            "visible_emotions": ["content", "peaceful", "affectionate"],
        },

        "emotional_vibe": {
            "overall_mood": "warm and nostalgic",
            "energy_level": "calm and gentle",
        },
    }

    print("\n=== Running Workflow Locally ===\n")

    result = await graph.ainvoke(
        {"video_json": input_json},
        {"configurable": {"thread_id": "local_test_1"}},
    )
    print(result)


asyncio.run(test_run())
