import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)
    args = sys.argv[1:]

    prompt = args[0] if len(args) >= 1 else sys.exit("Error: provide a prompt argument\nUsage: python main.py <prompt> [--flags...]") 

    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
    ]

    flags = args[1:]
    generate_content(client, messages, prompt, flags)

def generate_content(client, messages, prompt, flags):
    flags = check_flags(flags)

    MODEL = "gemini-2.0-flash-001"
    SEPARATOR = "=" * 30

    print_separator = lambda func: print(func, f"\n{SEPARATOR}")

    response = client.models.generate_content(
        model = MODEL,
        contents = messages,
    )
    
    if flags["--verbose"][1]:
        print_separator(f"User prompt: {prompt}")
        prompt_token_count = response.usage_metadata.prompt_token_count
        response_token_count = response.usage_metadata.candidates_token_count
        print_separator(f"Prompt tokens: {prompt_token_count}")
        print_separator(f"Response tokens: {response_token_count}")

    print_separator(f"Response: {response.text}")

def check_flags(flags):
    defined_flags = {
        "--verbose": [None, False],
    }
    i = 0

    if len(flags) == 0:
        return defined_flags

    if len(flags) == 1:
        if (flags[0] not in defined_flags and flags[0].startswith("--")) or (not flags[0].startswith("--")):
            sys.exit(f"Error: invalid [{flags[0]}] flag\nUsage: python main.py <prompt> [--flags...]")
        if flags[0] in defined_flags:
            defined_flags[flags[i]][1] = True

        return defined_flags

    while i < (len(flags) - 1):
        if (flags[i] not in defined_flags and flags[i].startswith("--")):
            sys.exit(f"Error: invalid [{flags[i]}] flag\nUsage: python main.py <prompt> [--flags...]")

        if flags[i] in defined_flags:
            defined_flags[flags[i]][1] = True

        if (not flags[i + 1].startswith("--")):
            defined_flags[flags[i]][0] = flags[i + 1]
            i += 1
 
    return defined_flags

if __name__ == "__main__":
    main()
