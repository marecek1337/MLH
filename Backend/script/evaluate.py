import base64
import requests
import sys
import json
from PIL import Image
import io

# Check for the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <description> <max_score>")
    sys.exit(1)

# Extract arguments
description = sys.argv[1]
max_score = sys.argv[2]

# OpenAI API Key
api_key = "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"

def encode_image(image_path, output_size=(600, 400), quality=50):
    """Resize and encode the image to base64 with adjustable quality.
    The output_size and quality are more aggressively adjusted to reduce the request size."""
    with Image.open(image_path) as img:
        img = img.resize(output_size)  # Removed Image.ANTIALIAS
        
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)  # Further reduce quality
        buffer.seek(0)
        
        return base64.b64encode(buffer.read()).decode('utf-8')


# Path to your image
image_path = "f.jpg"

# Getting the base64 string after resizing and encoding with further reduced quality
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Update the payload with the description and max_score from the command line arguments
payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": f"{description}, with a max score of {max_score}."
      },
      {
        "role": "system",
        "content": f"data:image/jpeg;base64,{base64_image}"
      }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Check if response is successful
if response.status_code == 200:
    # Save response to a JSON file
    with open('response.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
    print("Response saved to response.json")
else:
    print(f"Failed to get a response from the OpenAI API: {response.text}")
