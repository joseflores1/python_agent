
import os
from pathlib import PurePath


def get_files_info(working_directory, directory = "."):

    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    p = PurePath(target_dir)
    if not p.is_relative_to(abs_working_dir):
        return  f'Error: cannot list "{directory}" directory as it is outside the permitted working directory'

    try:
        content_dir = os.listdir(target_dir)
        files_info = []
        for content in content_dir:
            content_path = os.path.join(target_dir, content)
            files_info.append(f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}")

        return "\n".join(files_info)

    except Exception as e:
        return f"Error listing files: {e}"