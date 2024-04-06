import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "f.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": "rate this ux/ui?"
        },
        {
            "role": "system",
            "content": f"data:image/jpeg;base64,{base64_image}"
        }
    ],
    "max_tokens": 300
}


response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())