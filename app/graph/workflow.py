from langgraph.graph import StateGraph
from langsmith import trace

from app.graph.node import context_node, emotion_node, final_composer, poem_analyzer, tone_node
from app.graph.state import PoemState
from langgraph.checkpoint.memory import MemorySaver

workflow = StateGraph(PoemState)

workflow.add_node("context_node", context_node)
workflow.add_node("emotion_node", emotion_node)
workflow.add_node("poem_analyzer", poem_analyzer)
workflow.add_node("tone_node", tone_node)
workflow.add_node("final_composer", final_composer)

workflow.set_entry_point("context_node")

workflow.add_edge("context_node", "emotion_node")
workflow.add_edge("emotion_node", "poem_analyzer")
workflow.add_edge("poem_analyzer", "tone_node")
workflow.add_edge("tone_node", "final_composer")

graph = workflow.compile(checkpointer=MemorySaver())

# # ----------------------
# # 2. Add LangSmith tracing
# # ----------------------


# @trace(name="poetry_workflow_run")
# async def run_workflow(input_json):
#     result = await graph.ainvoke({"video_json": input_json})
#     return result
