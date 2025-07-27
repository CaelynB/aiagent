import os

# function to write or overwrite content to the specified file
def write_file(working_directory, file_path, content):
    # construct the target file path relative to the working directory
    relative_path = os.path.join(working_directory, file_path)

    # get the absolute paths for the working directory and the target file
    working_directory_abspath = os.path.abspath(working_directory)
    file_abspath = os.path.abspath(relative_path)

    # if the target file is outside the permitted working directory, return an error message
    if not file_abspath.startswith(working_directory_abspath):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # if the target path doesn't exist
    if not os.path.exists(file_abspath):
        # attempt to create the parent directory structure for the target file
        try:
            os.makedirs(os.path.dirname(file_abspath), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    
    # if the target path exists and is a directory, return an error message
    if os.path.exists(file_abspath) and os.path.isdir(file_abspath):
        return f'Error: "{file_path}" is a directory, not a file'

    # attempt to write or overwrite content to the target file
    try:
        # open the file in write mode
        with open(file_abspath, 'w') as f:
            # write the content to the file
            f.write(content)

        # return a success message with the number of characters written
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
