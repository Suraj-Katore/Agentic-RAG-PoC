from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.in_memory import InMemoryDb

# Your Groq API key
GROQ_API_KEY = "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"

# Initialize in-memory database for session memory
memory_db = InMemoryDb()

# Initialize the Groq model
model = Groq(
    id="llama-3.3-70b-versatile",  # Replace with your desired Groq model ID
    api_key=GROQ_API_KEY       # Pass the Groq key directly
)

# Initialize the agent
agent = Agent(
    model=model,
    db=memory_db,
    tools=[DuckDuckGoTools()],
    enable_user_memories=True,
    add_history_to_context=True,
    markdown=True,
    #debug_mode=True
)

if __name__ == "__main__":
    # First query: recipe + nutritional info
    agent.print_response(
        "I'm vegetarian. Suggest me a quick healthy recipe using oats and bananas, and find the latest nutritional info online.",
        stream=True
    )

    # Follow-up query using memory
    agent.print_response(
        "Now suggest a lunch plan for me keeping my vegetarian preference in mind.",
        stream=True
    )






