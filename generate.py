from google.genai import types

from config import MODEL, SYSTEM_PROMPT, print_separator
from flags import check_args
from call_function import available_functions, call_function

def generate_content(client, messages, prompt, args):
    flags = check_args(args)

    response = client.models.generate_content(
        model = MODEL,
        contents = messages,
        config = types.GenerateContentConfig(system_instruction = SYSTEM_PROMPT, tools = [available_functions])
    )
    
    verbose_set = flags["--verbose"][1]

    if verbose_set:
        print_separator(f"User prompt: {prompt}")
        prompt_token_count = response.usage_metadata.prompt_token_count
        response_token_count = response.usage_metadata.candidates_token_count
        print_separator(f"Prompt tokens: {prompt_token_count}")
        print_separator(f"Response tokens: {response_token_count}")

    function_calls = response.function_calls

    if function_calls:
        for function_call in function_calls:
            function_call_result = call_function(function_call, verbose = verbose_set)

            if (
                not function_call_result.parts
                or
                not function_call_result.parts[0]
                or 
                not function_call_result.parts[0].function_response
            ):
                raise Exception("empty function call result")

            specific_result = function_call_result.parts[0].function_response.response
 
            if verbose_set:
                print_separator(f"{specific_result["result"]}")
    else:
        return response.text
