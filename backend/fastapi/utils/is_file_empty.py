from utils.states import ResumeAnalyserState
from langgraph.graph import END
def is_file_empty(state: ResumeAnalyserState)->str:
    print("============= is_file_empty checked ================")
    if state["file_empty"]:
        return END
    else:
        return "llm_response"