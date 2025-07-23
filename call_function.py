from google.genai import types

from config import CWD, print_separator
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations = [
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

FUNCTION_DICT = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(function_call_part: types.FunctionCall, verbose = False):
    function_name = function_call_part.name
    if function_name not in FUNCTION_DICT:
        return types.Content(
            role = "tool",
            parts = [
                types.Part.from_function_response(
                    name = function_name,
                    response = {"error": f"Unknown function {function_name}" },
                ),
            ],
        )

    function_args = function_call_part.args
    if verbose:
        print_separator(f"Calling function: {function_name}({function_args})")
    else:
        print_separator(f"- Calling function: {function_name}")

    cwd_dict = {"working_directory": CWD}
    function_args.update(cwd_dict)
    function_to_run = FUNCTION_DICT[function_name]

    function_result = function_to_run(**function_args) 

    return types.Content(
        role = "tool",
        parts = [
            types.Part.from_function_response(
                name = function_name,
                response = {"result": function_result},
            ),
        ],
    )
