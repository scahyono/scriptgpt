from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration Management: Load API key from environment variables
api_key = os.environ.get('OPENAI_API_KEY')
MODEL="gpt-4-1106-preview" # Update this to the desired model version

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def scriptgpt_response(user_input):
    """Generate a response to the user input using OpenAI API."""
    user_input = user_input.lower()

    try:
        # Connect to the OpenAI API and get a response using the updated method
        instruction = "ScriptGPT specializes in creating and optimizing scripts for automation and integration tasks. It provides complete, ready-to-use scripts and offers suggestions for script improvements. Knowledgeable in various scripting languages, it addresses both simple and complex automation needs. While not executing scripts, Script Automator delivers secure, efficient, and best practice-oriented code solutions. If a user's request lacks specific details, it will ask for clarification to ensure accuracy and helpfulness. The interaction style is direct and practical, aiming to provide scripts efficiently. For users who need it, Script Automator can also include brief explanations or comments within the scripts, particularly useful for those less experienced in scripting."

        chat_completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_input}
            ]
        )
        response_content = chat_completion.choices[0].message.content.strip()

    except Exception as e:
        return f"An error occurred: {e}"

    return response_content

def chat():
    print("What automation or integration script do you need? Type 'bye' to exit.")

    while True:
        user_input = input("\033[92mYou: \033[0m")  # \033[92m is the ANSI escape code for green text, \033[0m resets the text color
        if user_input.lower() in ('bye', 'exit', 'quit'):
            print(f"\033[94mScriptGPT: \033[0mGoodbye! Have a nice day!")  # \033[94m is the ANSI escape code for blue text
            break
        response = scriptgpt_response(user_input)
        print(f"\033[94mScriptGPT: \033[0m{response}")

chat()