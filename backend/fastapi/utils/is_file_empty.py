from utils.states import ResumeAnalyserState
from langgraph.graph import END
def is_file_empty(state: ResumeAnalyserState)->str:
    if state["file_empty"]:
        return END
    else:
        return "llm_response"