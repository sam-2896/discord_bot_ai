import openai
import os 

from dotenv import load_dotenv

load_dotenv()
key = os.getenv("key")
openai.api_key = key # replace with your API key

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Example usage
def ask(inp):
    prompt = inp
    generated_text = generate_text(prompt)
    return generated_text

