import os
from google.genai import types
from pathlib import PurePath

schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "Writes/overwrites/creates a file given a content, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path of the file to be written, relative to the working directory.",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "The content to be written into the file."
            ),
        },
        required = ["file_path", "content"] 
    ),
)

def write_file(working_directory, file_path, content):
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    p = PurePath(target_dir)
    if not p.is_relative_to(abs_working_dir):
        return  f'Error: cannot write to {file_path}" as it is outside the permitted working directory'
   
    dir_name = os.path.dirname(target_dir)
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name, exist_ok = True)
        except Exception as e:
            return 'Error creating directory: {e}'

    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error writing file: {e}'