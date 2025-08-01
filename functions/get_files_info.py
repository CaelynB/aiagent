import os
from google.genai import types

# function to list the contents of a specified directory and return each file's metadata
def get_files_info(working_directory, directory="."):
    # construct the target directory path relative to the working directory
    relative_path = os.path.join(working_directory, directory)

    # get the absolute paths for the working directory and the target directory
    working_directory_abspath = os.path.abspath(working_directory)
    directory_abspath = os.path.abspath(relative_path)

    # if the target directory is outside the permitted working directory, return an error message
    if not directory_abspath.startswith(working_directory_abspath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # if the target path is not a directory, return an error message
    if not os.path.isdir(directory_abspath):
        return f'Error: "{directory}" is not a directory'

    # attempt to list the files in the target directory and return their metadata
    try:
        # initialize an empty list to store the metadata for each file
        files_info = []

        # for each file in the target directory
        for file in os.listdir(directory_abspath):
            # build the full path to the file
            filepath = os.path.join(directory_abspath, file)

            # get the file size and whether it's a directory
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)

            # append the file's metadata to the list
            files_info.append(
                f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )

        # return the file metadata as a single formatted string
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

"""
builds a function declaration (schema) for the get_files_info function that the Gemini model can call
this schema tells the Gemini model what the function does and what parameters it accepts
"""
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
