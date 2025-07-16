import os
from dotenv import load_dotenv
from google import genai

def main():
    # load environment variables from the .env file
    load_dotenv()

    # read the API key
    api_key = os.environ.get("GEMINI_API_KEY")

    # create a new instance of a Gemini client using the API key
    client = genai.Client(api_key=api_key)

    # generate a response from the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print(f"Response: {response.text}")

    # print usage metadata
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
