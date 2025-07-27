import os
from config import MAX_CHARS

# function to read the contents of a specified file and return it's content as a string
def get_file_content(working_directory, file_path):
    # construct the target file path relative to the working directory
    relative_path = os.path.join(working_directory, file_path)

    # get the absolute paths for the working directory and the target file
    working_directory_abspath = os.path.abspath(working_directory)
    file_abspath = os.path.abspath(relative_path)

    # if the target file is outside the permitted working directory, return an error message
    if not file_abspath.startswith(working_directory_abspath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # if the target path is not a file, return an error message
    if not os.path.isfile(file_abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # attempt to read the target file and return its content
    try:
        # open the file in read mode
        with open(file_abspath, "r") as f:
            # read the content of the file, limiting to MAX_CHARS characters
            file_content_string = f.read(MAX_CHARS)

            # if the file's content exceeds the maximum allowed characters, append a truncation message
            if os.path.getsize(file_abspath) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        # return the content of the file as a string
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
