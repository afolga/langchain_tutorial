import os
from langchain_core.prompts import PromptTemplate

# Mock ChatGroq class (already provided)
class ChatGroq:
    """Mock ChatGroq class for educational purposes."""

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]
        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")

    def invoke(self, messages):
        """Mock invoke method that returns a simulated response."""
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Messages must be a non-empty list")
        # Simulate responses based on model
        if self.model == "llama-4-8b-instant":
            content = "[Llama 4 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
        elif self.model == "llama-3.3-70b-versatile":
            if self.temperature > 0.2:
                content = "[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            else:
                content = "[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"
        return MockAIMessage(content)


class MockAIMessage:
    """Mock AI message response."""
    def __init__(self, content):
        self.content = content


# ----------------- Implementations -----------------

def implement_set_api_key(api_key: str):
    """Set the GROQ_API_KEY environment variable."""
    os.environ["GROQ_API_KEY"] = api_key


def implement_llama_4_model():
    """Return a ChatGroq instance for Llama 4."""
    return ChatGroq(model="llama-4-8b-instant", temperature=0)


def implement_llama_3_3_model():
    """Return a ChatGroq instance for Llama 3.3 with slightly creative responses."""
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)


def implement_query_model(model: ChatGroq, prompt: str):
    """Send a query to the model and return the response content."""
    # Wrap the prompt in a list (ChatGroq expects a list)
    response = model.invoke([prompt])
    return response.content


def implement_compare_models(prompt: str):
    """Query both models and return a dictionary of responses."""
    results = {}
    llama4 = implement_llama_4_model()
    llama33 = implement_llama_3_3_model()
    results["llama-4-8b-instant"] = implement_query_model(llama4, prompt)
    results["llama-3.3-70b-versatile"] = implement_query_model(llama33, prompt)
    return results

def main():
    print("🚀 Groq Model Switching Exercise")

    implement_set_api_key("mock_api_key_for_testing")
    print("✓ API key set:", os.environ.get("GROQ_API_KEY"))

    prompt = "Explain the concept of machine learning in one sentence."

    llama4 = implement_llama_4_model()
    llama33 = implement_llama_3_3_model()

    print("Llama 4:", implement_query_model(llama4, prompt))
    print("Llama 3.3:", implement_query_model(llama33, prompt))

    comparison = implement_compare_models(prompt)
    print("Comparison Results:")
    for model, response in comparison.items():
        print(f"{model}: {response}")


if __name__ == "__main__":
    main()
