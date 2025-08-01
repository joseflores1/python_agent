import os
from google.genai import types
from pathlib import PurePath

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description = f"Reads and returns at max {MAX_CHARS} characters from a specified file within and constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path to the file  whose content needs to be read, relative to the working directory.",
            ),
        },
        required = ["file_path"]
    ),
)

def get_file_content(working_directory, file_path):
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    if not os.path.isfile(target_dir):
        return f'File not found or it is not a regular file: "{file_path}"'

    p = PurePath(target_dir)
    if not p.is_relative_to(abs_working_dir):
        return  f'Error: cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_dir, mode = 'r') as f:
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string

    except Exception as e:
        return f"Error getting file {file_path} content: {e}"
