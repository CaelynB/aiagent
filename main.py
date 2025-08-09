import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file
from config import WORKING_DIRECTORY

def main():
    # load the environment variables from the .env file
    load_dotenv()

    # read the API key
    api_key = os.environ.get("GEMINI_API_KEY")

    # create a new instance of a Gemini client using the API key
    client = genai.Client(api_key=api_key)

    # initialize verbose mode to false
    verbose_enabled = False

    # if the verbose flag is present in the command line arguments, set verbose mode to true
    if "--verbose" in sys.argv:
        verbose_enabled = True

    # initialize an empty list for command line arguments
    arguments = []

    # for each argument in the command line arguments after the script name
    for arg in sys.argv[1:]:
        # if the argument doesn't match the verbose flag, append it to the arguments list
        if arg != "--verbose":
            arguments.append(arg)

    # if no command line arguments are provided, print usage instructions and exit
    if not arguments:
        print("Usage: python main.py <prompt> [--verbose]")
        sys.exit(1)

    # join the command line arguments to form the user prompt
    user_prompt = " ".join(arguments)

    # if verbose mode is enabled, print the user prompt
    if verbose_enabled:
        print(f"User prompt: {user_prompt}")

    # create a list of messages with the user prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # define a system prompt that instructs the Gemini model on its constraints and capabilities
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    # create a list of all the functions available to the Gemini model
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    # get a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    # initialize an empty list to store function responses
    function_responses = []

    # if the response from the Gemini model contains any function calls
    if response.function_calls:
        # for each function call in the response
        for function_call_part in response.function_calls:
            # call the function with the provided arguments and store the result
            function_call_result = call_function(function_call_part, verbose_enabled)

            # if the result is empty or missing a function response, raise an exception
            if not function_call_result.parts or not function_call_result.parts[0].function_response:
                raise Exception("empty function call result")

            # if verbose mode is enabled, print the response returned by the function
            if verbose_enabled:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            # append the result to the list of function responses
            function_responses.append(function_call_result.parts[0])
    # otherwise, just print the response
    else:
        print(f"Response: {response.text}")

    # if the list of function responses is empty, raise an exception
    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    # if verbose mode is enabled, print the number of tokens consumed
    if verbose_enabled:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# function to call the appropriate function based on the provided function call part
def call_function(function_call_part, verbose_enabled=False):
    # get the function name and arguments from the function call
    function_name = function_call_part.name
    function_args = dict(function_call_part.args)

    # if verbose mode is enabled, print the function name and arguments
    if verbose_enabled:
        print(f"Calling function: {function_name}({function_args})")
    # otherwise, just print the function name
    else:
        print(f" - Calling function: {function_name}")

    # create a dictionary to map available function names to their corresponding implementations
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    # if the function name is not in the function map dictionary, return an error message
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # add the working directory to the function arguments dictionary
    function_args["working_directory"] = WORKING_DIRECTORY

    # call the mapped function based on the function name with the keyword arguments
    function_result = function_map[function_name](**function_args)

    # return the result of the function call
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

if __name__ == "__main__":
    main()
