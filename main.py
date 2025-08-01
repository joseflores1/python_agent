import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_ITER, print_separator
from generate import generate_content

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)
    args = sys.argv[1:]

    prompt = args[0] if len(args) >= 1 else sys.exit("Error: provide a prompt argument\nUsage: python main.py <prompt> [--args...]") 

    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
    ]

    args = args[1:]
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITER:
            print(f"Maximum iterations ({MAX_ITER}) reached.")
        try:
            response_text, new_messages = generate_content(client, messages, args)
            if response_text:
                print_separator(response_text)
                break
            messages = new_messages

        except Exception as e:
            sys.exit(f"LLM couldn't generate response: {e}")

if __name__ == "__main__":
    main()
