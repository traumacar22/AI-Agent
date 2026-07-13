import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from system_prompt import system_prompt
from call_function import *

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
    ]
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages = messages,
            temperature = 0,
            tools = available_functions,
        )

        #print(f"Model used: {response.model}") #this line is for in case you want to troubleshoot how different models are performing

        message = response.choices[0].message
        messages.append(message) #keeping track of Agent responses

        if message.tool_calls: #this is a truthy check. If there is a value then true basically
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message) #keeping track of Agent responses
                if args.verbose == True:
                    print(f"-> {result_message['content']}")
        else:
            print(message.content)
            break

if __name__ == "__main__":
    main()
