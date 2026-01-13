from agent.graph import agent_graph

state = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "lead_captured": False
}

print("🚀 AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    state["messages"].append(user_input)
    state = agent_graph.invoke(state)
