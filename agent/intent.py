from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0
)

INTENT_PROMPT = """
You are classifying user intent for a SaaS sales agent.

Classify the user's intent into EXACTLY one of:
- greeting
- product_inquiry
- high_intent_lead

Definitions:
- greeting: casual hello, general interest, asking what the product is
- product_inquiry: asking about features, pricing, plans, policies
- high_intent_lead: user expresses desire to try, sign up, start, use, or buy a plan
  Examples of high intent phrases:
  - "I want to try"
  - "I want the Pro plan"
  - "I want to sign up"
  - "This sounds good"
  - "I’m interested in using this"

Conversation so far:
{history}

Latest user message:
"{message}"

Respond with ONLY one label.
"""

def detect_intent(message: str, history: list[str]) -> str:
    prompt = INTENT_PROMPT.format(
        message=message,
        history="\n".join(history[-4:])
    )
    response = llm.invoke(prompt)
    return response.content.strip().lower()
