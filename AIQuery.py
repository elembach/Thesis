import openai
import json
import random
openai.api_key = "org-ZOlnq2F66CHgPpvocB7gw4O6"


# Load prompts from a file (one prompt per line)
with open('prompts.txt', 'r') as file:
    prompts = file.readlines()

responses = []


# Define function to get response from ChatGPT
def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" depending on model
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


# Get and save responses to JSON and text files
for prompt in prompts:
    response = get_chatgpt_response(prompt.strip())
    responses.append({"prompt": prompt.strip(), "response": response})

    # Append response to text file
    with open("responses.txt", "a") as text_file:
        text_file.write(f"Prompt: {prompt}\nResponse: {response}\n\n")

# Save all responses to a JSON file
with open("responses.json", "w") as json_file:
    json.dump(responses, json_file, indent=4)
