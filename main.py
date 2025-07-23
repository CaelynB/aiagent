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

    # if no command line arguments are provided after the script name, print usage instructions and exit
    if not sys.argv[1:]:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    # join the command line arguments after the script name to form the user prompt
    user_prompt = " ".join(sys.argv[1:])

    # create a list of messages with the user prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # get a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    # print the response and the number of tokens consumed
    print(f"Response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
