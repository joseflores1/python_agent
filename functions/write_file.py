import os
from pathlib import PurePath

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