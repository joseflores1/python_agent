from google.genai import types

from config import SEPARATOR, MODEL, SYSTEM_PROMPT
from flags import check_args
from call_function import available_functions

def generate_content(client, messages, prompt, args):
    flags = check_args(args)

    print_separator = lambda func: print(func, f"\n{SEPARATOR}")

    response = client.models.generate_content(
        model = MODEL,
        contents = messages,
        config = types.GenerateContentConfig(system_instruction = SYSTEM_PROMPT, tools = [available_functions])
    )
    
    if flags["--verbose"][1]:
        print_separator(f"User prompt: {prompt}")
        prompt_token_count = response.usage_metadata.prompt_token_count
        response_token_count = response.usage_metadata.candidates_token_count
        print_separator(f"Prompt tokens: {prompt_token_count}")
        print_separator(f"Response tokens: {response_token_count}")

    function_calls = response.function_calls

    if function_calls:
        for function_call in function_calls:
            print_separator(f"Calling function: {function_call.name}({function_call.args})")

    else:
        return response.text
