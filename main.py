import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

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

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    # create a list of all the functions available to the Gemini model
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info
        ]
    )

    # get a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    # if the response from the Gemini model contains any function calls
    if response.function_calls:
        # for each function call in the response, print its name and arguments
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    # otherwise, just print the response
    else:
        print(f"Response: {response.text}")

    # if verbose mode is enabled, print the number of tokens consumed
    if verbose_enabled:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
