import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    print_separator = lambda func: print(func, f"\n{SEPARATOR}")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)

    PROMPT = sys.argv[1] if len(sys.argv) >= 2 else sys.exit("Error: provide a prompt argument\nUsage: python main.py <prompt>") 
    MODEL = "gemini-2.0-flash-001"
    SEPARATOR = "=" * 30

    response = client.models.generate_content(model = MODEL, contents = PROMPT)

    print_separator("PROMPT:")
    print_separator(PROMPT)

    print_separator("RESPONSE:")
    print_separator(response.text)

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    print_separator(f"Prompt tokens: {prompt_token_count}")
    print_separator(f"Response tokens: {response_token_count}")

if __name__ == "__main__":
    main()
