from agent.intent import detect_intent
from agent.tools import mock_lead_capture

def intent_node(state):
    message = state["messages"][-1]
    intent = detect_intent(message, state["messages"])

    # Override greeting if message also asks about product/pricing
    lower_msg = message.lower()
    if intent == "greeting" and any(
        keyword in lower_msg
        for keyword in ["price", "pricing", "plan", "cost", "features"]
    ):
        intent = "product_inquiry"

    state["intent"] = intent

    return state


def greeting_node(state):
    print("Agent: Hi! I can help you with AutoStream pricing or features 😊")
    return state

def rag_node(state, retriever):
    query = state["messages"][-1]
    docs = retriever.invoke(query)
    context = "\n".join(d.page_content for d in docs)

    print(f"Agent:\n{context}")
    return state


def lead_node(state):
    if not state["name"]:
        state["name"] = input("Agent: What's your name?\nUser: ")
        return state

    if not state["email"]:
        state["email"] = input("Agent: What's your email?\nUser: ")
        return state

    if not state["platform"]:
        state["platform"] = input("Agent: Which platform do you create on?\nUser: ")
        return state

    return state




def tool_node(state):
    if (
        state["name"]
        and state["email"]
        and state["platform"]
        and not state["lead_captured"]
    ):
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )
        state["lead_captured"] = True
        print("Agent: Thanks! Our team will reach out shortly 🚀")

    return state

