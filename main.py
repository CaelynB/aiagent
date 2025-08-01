import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

    # define a system prompt that instructs the model to ignore user input and respond with fixed message
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    # get a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    # print the response
    print(f"Response: {response.text}")

    # if verbose mode is enabled, print the number of tokens consumed
    if verbose_enabled:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
