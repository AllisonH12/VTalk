import os
import openai
import requests
from PIL import Image

# Replace 'your_api_key_here' with your actual API key
openai.api_key = "apikey"

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

# Test the function with a sample image
image_path = "your_sketch_image
