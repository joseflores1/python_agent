from flags import check_args

def generate_content(client, messages, prompt, args):
    flags = check_args(args)

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

    print_separator(f"Response:")
    print_separator(response.text)
