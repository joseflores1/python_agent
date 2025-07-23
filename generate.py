from google.genai import types
from google import genai
from config import MODEL, SYSTEM_PROMPT, print_separator
from flags import check_args
from call_function import available_functions, call_function

def generate_content(client: genai.Client, messages: list[types.Content], args: list[str]):

    flags = check_args(args)
    response = client.models.generate_content(
        model = MODEL,
        contents = messages,
        config = types.GenerateContentConfig(system_instruction = SYSTEM_PROMPT, tools = [available_functions])
    )
    
    candidates = response.candidates
    for candidate in candidates:
        messages.append(candidate.content)

    verbose_set = flags["--verbose"][1]

    function_calls = response.function_calls

    if function_calls:
        function_responses = []
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
            text_result = specific_result["result"]

            if verbose_set:
                print_separator(f"{text_result}")

            function_responses.append(function_call_result.parts[0])

        if not function_responses:
            raise Exception("no function responses generated, exiting.")

        messages.append(types.Content(role = "tool", parts = function_responses))

        return None, messages
    else:
        return response.text, messages
