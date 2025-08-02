import os
import subprocess
from google.genai import types

# function to run a specified Python file
def run_python_file(working_directory, file_path, args=[]):
    # construct the target file path relative to the working directory
    relative_path = os.path.join(working_directory, file_path)

    # get the absolute paths for the working directory and the target file
    working_directory_abspath = os.path.abspath(working_directory)
    file_abspath = os.path.abspath(relative_path)

    # if the target file is outside the permitted working directory, return an error message
    if not file_abspath.startswith(working_directory_abspath):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # if the target path doesn't exist, return an error message
    if not os.path.exists(file_abspath):
        return f'Error: File "{file_path}" not found.'
    
    # if the target file doesn't end with .py, return an error message
    if not file_abspath.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    # attempt to run the target Python file and return its output
    try:
        # construct the command to run the Python file
        command = ['python', file_abspath]

        # if additional arguments are provided, extend the command list with them
        if args:
            command.extend(args)

        # run the command, capturing output and errors, with a timeout
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory_abspath,
        )
        
        # initialize an empty list to hold the output
        output = []

        # if the result is a standard output, append it to the output list
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")

        # if the result is a standard error, append it to the output list
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        # if the process exited with a non-zero code, append an error message to the output list
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        # if no output is produced, return a message
        if not output:
            return "No output produced."

        # return combined output
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"

# builds a function declaration (schema) for the run_python_file function that the Gemini model can call
# this schema tells the Gemini model what the function does and what parameters it accepts
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
