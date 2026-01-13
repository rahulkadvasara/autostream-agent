from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import (
    intent_node,
    greeting_node,
    rag_node,
    lead_node,
    tool_node
)
from agent.rag import build_vectorstore

vectorstore = build_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

def route(state):
    if state["lead_captured"]:
        if state["intent"] == "greeting":
            return "greeting"
        return "rag"

    if state["name"] or state["email"] or state["platform"]:
        return "lead"

    if state["intent"] == "greeting":
        return "greeting"

    if state["intent"] == "high_intent_lead":
        return "lead"

    return "rag"




def lead_router(state):
    if state["name"] and state["email"] and state["platform"]:
        return "tool"
    return "lead"




graph = StateGraph(AgentState)

graph.add_node("intent", intent_node)
graph.add_node("greeting", greeting_node)
graph.add_node("rag", lambda s: rag_node(s, retriever))
graph.add_node("lead", lead_node)
graph.add_node("tool", tool_node)

graph.set_entry_point("intent")

graph.add_conditional_edges("intent", route)
graph.add_conditional_edges("lead", lead_router)

graph.add_edge("tool", END)
graph.add_edge("greeting", END)
graph.add_edge("rag", END)



agent_graph = graph.compile()
