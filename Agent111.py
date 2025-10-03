import os
import warnings
from agno.models.groq import Groq
from agno.agent.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

# --- Suppress httpx resource warnings ---
warnings.simplefilter("ignore", ResourceWarning)

# --- Set your Groq API key here ---
os.environ["GROQ_API_KEY"] = "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"

# --- Initialize Groq model ---
model = Groq("llama-3.3-70b-versatile")

# --- Initialize DuckDuckGo tool ---
ddg_tool = DuckDuckGoTools()

# --- Initialize Agent with model and tool ---
agent = Agent(model=model, tools=[ddg_tool])

# --- Function to query the agent ---
def ask(prompt: str):
    try:
        response = agent.run(prompt)
        # Extract clean content
        output_text = getattr(response, "content", str(response))
        print("\n--- Response ---\n")
        print(output_text.strip())
        print("\n----------------\n")
    except Exception as e:
        print(f"Error: {e}")

# --- Interactive chatbot ---
if __name__ == "__main__":
    print("Welcome to the Chatbot! What's the agenda today? (type 'exit' to quit)\n")
    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            if user_input:
                ask(user_input)
    finally:
        # Properly close the Groq client
        if hasattr(model, "client") and model.client is not None:
            model.client.close()
        print("\nChatbot session ended.")




