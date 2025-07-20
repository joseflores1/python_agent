import os
import subprocess
from pathlib import PurePath

from config import TIMEOUT_SECONDS, RUN_CMD

def run_python_file(working_directory, file_path, args = []):
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    p = PurePath(target_dir)
    if not p.is_relative_to(abs_working_dir):
        return  f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
   
    if not os.path.exists(target_dir):
        return f'Error: File "{file_path}" not found.'

    if os.path.isdir(target_dir):
        return f'Error: "{file_path}" is a directory, not a file.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        args = [*RUN_CMD, target_dir] + args
        completed_process = subprocess.run(args = args, capture_output = True, timeout = TIMEOUT_SECONDS, cwd = abs_working_dir, text = True)    
        exit_code = completed_process.returncode

        stdout = completed_process.stdout
        stderr = completed_process.stderr
        len_out = len(stdout)
        len_err = len(stderr)

        has_stdout = f"STDOUT:\n{stdout}\n" if len_out != 0 else ""
        has_stderr = f"STDERR:\n{stderr}\n" if len_err != 0 else ""
        non_zero_exit = f"Process exited with code {exit_code}\n" if exit_code != 0 else ""

        return (has_stdout + has_stderr + non_zero_exit) if (len(has_stdout + has_stderr + non_zero_exit) != 0) else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"