Poetry Subgraph Workflow

This repository implements a Poetry Generation Workflow using LangGraph and LangSmith. It processes structured video input to generate poetry based on scene, human presence, and emotional vibes using Google Gemini LLM.

Table of Contents

Features

Tech Stack

Installation

Setup

Running the Workflow Locally

Project Structure

Contributing

Features

Extract context from a video scene (context_node)

Analyze emotions (emotion_node)

Analyze poem structure (poem_analyzer)

Determine tone (tone_node)

Compose final poem (final_composer)

Local testing using LangGraph

Optional tracing using LangSmith

Tech Stack

Python 3.11+

LangGraph – Graph-based workflow orchestration

LangSmith – Tracing and monitoring workflow runs

Google Gemini API – LLM for content generation

Pydantic – Data validation

asyncio – Asynchronous execution

Installation

Clone the repository:

git clone https://github.com/yourusername/poetry-subgraph.git
cd poetry-subgraph


Create a virtual environment and activate:

conda create -n memevid python=3.11 -y
conda activate memevid


Install dependencies:

pip install -r requirements.txt

Setup

Create a .env file in the root of the project:

touch .env


Add the required API keys:

GOOGLE_API_KEY=your_google_gemini_api_key
LANGCHAIN_API_KEY=your_langchain_api_key


Load environment variables:

# For Windows (PowerShell)
setx GOOGLE_API_KEY "your_google_gemini_api_key"
setx LANGCHAIN_API_KEY "your_langchain_api_key"

# For Unix / Mac
export GOOGLE_API_KEY="your_google_gemini_api_key"
export LANGCHAIN_API_KEY="your_langchain_api_key"

Running the Workflow Locally

Use the provided test runner:

python -m app.langsmith


The test_run function uses a sample video_json input, for example:

{
  "scene": {
    "setting": "beach",
    "time_of_day": "sunset",
    "season": "summer",
    "natural_elements": ["ocean waves", "golden sky", "soft breeze"],
    "objects_in_scene": ["wooden bench", "sand", "distant boats"]
  },
  "human_presence": {
    "people_count": 1,
    "social_context": "solo relaxation",
    "activities": ["sitting", "watching the sunset", "thinking quietly"],
    "visible_emotions": ["peaceful", "calm", "reflective"]
  },
  "emotional_vibe": {
    "overall_mood": "serene",
    "energy_level": "low and soothing"
  }
}


Workflow nodes run asynchronously:

context_node → emotion_node → poem_analyzer → tone_node → final_composer

Output will include the final poem in JSON format:

{
  "final_poem": "Your generated poem here..."
}

Project Structure
poetry-subgraph/
├─ app/
│  ├─ graph/
│  │  ├─ workflow.py       # LangGraph workflow setup
│  │  ├─ node.py           # Node functions
│  │  └─ state.py          # PoemState and VideoState definitions
│  ├─ services/
│  │  ├─ extract_context.py
│  │  ├─ extract_emotion.py
│  │  ├─ extract_tone.py
│  │  └─ compose_poem.py
│  ├─ llm.py               # Google Gemini wrapper (_generate)
│  ├─ prompt.py            # Node prompts
│  └─ langsmith.py         # Local test runner & optional LangSmith tracing
├─ .env
└─ requirements.txt