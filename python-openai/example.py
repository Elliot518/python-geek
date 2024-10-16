import openai
import os

# Set your OpenAI API key, either from an environment variable or directly
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simple completion request to test the API
try:
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Use gpt-3.5-turbo, which is available in free tiers
        prompt="Hello World",
        max_tokens=5  # Limiting token usage
    )

    # Print the response from the API
    print(response['choices'][0]['text'].strip())

except openai.error.RateLimitError:
    print("You have exceeded your free quota. Please check your plan or wait for the next reset.")
except openai.error.AuthenticationError:
    print("There was an issue with your API key. Please check if it's set correctly.")
except Exception as e:
    print(f"An error occurred: {e}")

