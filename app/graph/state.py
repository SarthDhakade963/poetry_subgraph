from typing import List, Optional
from pydantic import BaseModel
from typing import TypedDict, List, Optional

class VideoState(BaseModel):
    # Scene fields
    setting: Optional[str] = None
    time_of_day: Optional[str] = None
    season: Optional[str] = None
    natural_elements: Optional[List[str]] = None
    objects_in_scene: Optional[List[str]] = None

    # Human presence fields
    people_count: Optional[int] = None
    social_context: Optional[str] = None
    activities: Optional[List[str]] = None
    visible_emotions: Optional[List[str]] = None

    # Emotional vibe
    overall_mood: Optional[str] = None
    energy_level: Optional[str] = None


class PoemState(TypedDict, total=False):
    # Context Node
    core_message: str
    moment_description: str
    underlying_theme: str

    # Emotion Node
    primary_emotion: str
    secondary_emotions: List[str]
    emotional_arc: str
    emotional_intensity: Optional[float]

    # Poem Analyzer
    central_theme: str
    mood: str
    narrative_voice: str

    # Tone Node
    selected_tone: str

    # Final Poem
    final_poem: str

    # Input
    video_json: Optional[VideoState]
