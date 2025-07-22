MAX_CHARS = 10000
TIMEOUT_SECONDS = 30
SEPARATOR = "=" * 30
MODEL = "gemini-2.0-flash-001"
RUN_CMD = ["uv", "run"]
SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
CWD = "./calculator"

#Functions
print_separator = lambda func: print(func, f"\n{SEPARATOR}")