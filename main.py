import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # load environment variables from the .env file
    load_dotenv()

    # read the API key
    api_key = os.environ.get("GEMINI_API_KEY")

    # create a new instance of a Gemini client using the API key
    client = genai.Client(api_key=api_key)

    # check if the verbose flag is present in the command line arguments
    verbose = "--verbose" in sys.argv

    # initialize an empty list for command line arguments
    arguments = []

    # for each argument in the command line arguments (excluding the script name)
    for argument in sys.argv[1:]:
        # if the argument does not start with "--", append it to the arguments list
        if not argument.startswith("--"):
            arguments.append(argument)

    # if no prompt is provided, print usage instructions and exit
    if not arguments:
        print("Usage: python main.py <prompt> [--verbose]")
        sys.exit(1)

    # join the command line arguments to form the user prompt
    user_prompt = " ".join(arguments)

    # if verbose flag is included, print the user prompt
    if verbose:
        print(f"User prompt: {user_prompt}")

    # create a list of messages with the user prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # generate a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print(f"Response: {response.text}")

    # if verbose flag is included, print usage metadata
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
