from typing import List, Optional
from pydantic import BaseModel, Field
from typing import TypedDict, List, Optional


class Scene(BaseModel):
    setting: Optional[str] = None
    time_of_day: Optional[str] = None
    season: Optional[str] = None
    location_type: Optional[str] = None
    natural_elements: Optional[List[str]] = None
    objects_in_scene: Optional[List[str]] = None


class Visual(BaseModel):
    lighting: Optional[str] = None
    color_palette: Optional[str] = None
    camera_style: Optional[str] = None
    shot_type: Optional[str] = None
    movement_in_frame: Optional[str] = None
    visual_textures: Optional[List[str]] = None


class HumanPresence(BaseModel):
    people_count: Optional[int] = None
    social_context: Optional[str] = None
    activities: Optional[List[str]] = None
    visible_emotions: Optional[List[str]] = None

class EmotionalVibe(BaseModel):
    energy_level: Optional[str] = None
    overall_mood: Optional[str] = None

class PoetryAndWholesomeReflection(BaseModel):
    melodic_elements: str
    atmospheric_details: List[str] = Field(default_factory=list)
    natural_imagery: List[str] = Field(default_factory=list)
    micro_movements: List[str] = Field(default_factory=list)
    textures: List[str] = Field(default_factory=list)
    emotional_purity: str

class GeneralAttributes(BaseModel):
    scene: Optional[Scene] = None
    visual: Optional[Visual] = None
    human_presence: Optional[HumanPresence] = None
    emotional_vibe: Optional[EmotionalVibe] = None

class QuoteTypeSpecific(BaseModel):
    poetry_and_wholesome_reflection: Optional[PoetryAndWholesomeReflection] = None

class VideoState(BaseModel):
    general_attributes: Optional[GeneralAttributes] = None
    quote_type_specific: Optional[QuoteTypeSpecific] = None
    metadata_tags: Optional[List[str]] = None

# class VideoState(BaseModel):
#     # Scene fields
#     setting: Optional[str] = None
#     time_of_day: Optional[str] = None
#     season: Optional[str] = None
#     natural_elements: Optional[List[str]] = None
#     objects_in_scene: Optional[List[str]] = None

#     # Human presence fields
#     people_count: Optional[int] = None
#     social_context: Optional[str] = None
#     activities: Optional[List[str]] = None
#     visible_emotions: Optional[List[str]] = None

#     # Emotional vibe
#     overall_mood: Optional[str] = None
#     energy_level: Optional[str] = None


class PoemState(BaseModel):
    video_json: Optional[VideoState]

    # Context Node
    core_message: Optional[str] = None
    moment_description: Optional[str] = None
    underlying_theme: Optional[str] = None

    # Emotion Node
    primary_emotion: Optional[str] = None
    secondary_emotions: List[str] = Field(default_factory=list)
    emotional_arc: Optional[str] = None
    emotional_intensity: Optional[float] = None

    # Poem Analyzer
    central_theme: Optional[str] = None
    mood: Optional[str] = None
    narrative_voice: Optional[str] = None

    # Tone Node
    selected_tone: Optional[str] = None

    # Final Poem
    final_poem: Optional[str] = None