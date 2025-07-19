import os

# function to get information about files in a specified directory
def get_files_info(working_directory, directory="."):
    # construct absolute paths for the working directory and target directory
    relative_path = os.path.join(working_directory, directory)
    working_directory_absolute_path = os.path.abspath(working_directory)
    target_directory_absolute_path = os.path.abspath(relative_path)

    # if the target directory is outside the permitted working directory, return an error message
    if not target_directory_absolute_path.startswith(working_directory_absolute_path):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    # if the target directory is not a directory, return an error message
    if not os.path.isdir(target_directory_absolute_path):
        return f"Error: '{directory}' is not a directory"
    
    # attempt to list files in the target directory and return their information
    try:
        # initialize an empty list to hold file information
        file_information = []

        # for each file in the target directory
        for file in os.listdir(target_directory_absolute_path):
            # construct the file path for the current file
            file_path = os.path.join(target_directory_absolute_path, file)

            # get the file size and whether it is a directory
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)

            # append the file information to the list
            file_information.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")

        # return the formatted file information as a string
        return "\n".join(file_information)
    except Exception as e:
        return f"Error listing files: {e}"