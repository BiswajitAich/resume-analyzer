from langgraph.graph import StateGraph, START, END
from utils.states import ResumeAnalyserState
from utils.extract_text_from_pdf import extract_text_from_pdf
from utils.is_file_empty import is_file_empty
from utils.llm import llm_response

graph = StateGraph(ResumeAnalyserState)

graph.add_node('extract_text_from_pdf', extract_text_from_pdf)
graph.add_node('llm_response', llm_response)

graph.add_edge(START, 'extract_text_from_pdf')
graph.add_conditional_edges(
    'extract_text_from_pdf', 
    is_file_empty,
    {
        END: END,
        'llm_response': 'llm_response'
    }
    )
graph.add_edge('llm_response', END)

workflow = graph.compile()