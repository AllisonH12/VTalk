import os
import openai
import requests
from PIL import Image
import base64
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key


def sketch_to_text(image_path):
    # Load the image and convert it to a URL
    image = Image.open(image_path)
    image.save("temp_image.png", "PNG")
    with open("temp_image.png", "rb") as f:
        img_url = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

    # Create a prompt for the OpenAI API
    prompt = f"A description of the sketch in the image: {img_url}"

    # Call the OpenAI API
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the text description from the response
    text_description = response.choices[0].text.strip()
    return text_description

def chat_with_gpt(text_description):
    # Define a chat prompt for the OpenAI API
    chat_prompt = f"I just saw an image described as: \"{text_description}\". Can you tell me more about it?"

    # Call the OpenAI API for a chat response
    chat_response = openai.Completion.create(
        engine="davinci-codex",
        prompt=chat_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the chat response
    chat_text = chat_response.choices[0].text.strip()
    return chat_text

# Test the functions with a sample image
image_path = "/Users/yonghuang/code/VTalk/images/sad.jpeg"
description = sketch_to_text(image_path)
print(f"Description: {description}")

# Use the description to prompt further conversation with ChatGPT
chat_response = chat_with_gpt(description)
print(f"ChatGPT Response: {chat_response}")
