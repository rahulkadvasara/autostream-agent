# 🚀 AutoStream AI Agent – Social-to-Lead Workflow

This project implements a **stateful, agentic conversational AI** that converts user conversations into **qualified business leads** for a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.

The agent is demonstrated via a **CLI-based interface**, focusing entirely on backend agent logic rather than frontend UI.

---

## 1️⃣ How to Run the Project Locally

### Prerequisites
- Python **3.9+**
- Groq Cloud API key
- Git

### Setup Steps

```bash
# Clone the repository
git clone <your-repo-url>
cd autostream-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1      # Windows
# source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Environment Variables
Create a .env file in the project root directory:
GROQ_API_KEY=your_groq_api_key_here

```
---
### Run The Agent
```bash
python main.py
```

### Expected Output

```bash
🚀 AutoStream AI Agent (type 'exit' to quit)
User:
```

---
## 2️⃣ Architecture Explanation

### 🔹 Why LangGraph?

LangGraph was chosen for this project because it enables **explicit, deterministic control over conversational workflows** using a **state-machine-based architecture**. Unlike simple chatbot loops or fully autonomous AutoGen-style agents, LangGraph allows precise control over **intent routing, multi-step workflows, and tool execution boundaries**.

This project requires strict guarantees that tools—such as lead capture—are executed **only when all required conditions are met**. LangGraph supports this by allowing developers to define **clear nodes, conditional transitions, and termination points**. This results in **predictable, debuggable, and production-ready agent behavior**, closely reflecting how real-world SaaS conversational agents are built.

---

### 🔹 How State Is Managed

The agent maintains a **shared state object** across conversation turns. This state stores:

- Conversation history  
- Detected user intent  
- Lead details (name, email, creator platform)  
- Lead capture status  

State persistence enables:
- Smooth **intent shifting** from product inquiry to high-intent lead  
- **Sequential lead qualification** without repetition  
- Prevention of **premature or duplicate tool execution**

After successful lead capture, the agent transitions into a **post-conversion support mode**, continuing to answer user questions without re-triggering lead collection. This mirrors **realistic SaaS sales and onboarding workflows**.


## 3️⃣ WhatsApp Deployment (Conceptual Explanation)

To deploy this agent on **WhatsApp**, the following architecture can be used:

### 📲 WhatsApp Business API / Twilio WhatsApp
- User messages are forwarded to a webhook endpoint.

### 🌐 Webhook Server (FastAPI / Flask)
- Receives incoming messages from WhatsApp.
- Uses the sender’s phone number as a session identifier.

### 🤖 Agent Integration
- The webhook forwards the message and the corresponding session state to the LangGraph agent.
- The agent processes the message using the stored state.

### 🧠 State Persistence
- Conversation state is stored in Redis or a database.
- Ensures continuity across multiple messages and sessions.

### 📤 Response Delivery
- Agent responses are sent back to the user via the WhatsApp API.

This architecture allows the **same agent logic** to be reused across platforms, with WhatsApp acting purely as a communication channel. It supports **scalability, persistent multi-turn conversations, and real-time lead capture from social interactions**.


## ✅ Key Features

- Intent detection (Greeting, Product Inquiry, High-Intent Lead)
- RAG-powered knowledge retrieval using a local knowledge base
- Multi-turn, stateful conversations
- Safe and gated lead capture tool execution
- CLI-based demonstration (no frontend)
