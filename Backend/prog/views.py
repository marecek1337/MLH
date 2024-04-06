import os
import random
import json
import base64
import requests
from django.http import HttpResponse
from django.conf import settings



def create_users(request):
    base_dir = os.path.join(settings.MEDIA_ROOT, 'storage')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Predefined lists of first and last names
    first_names = ["John", "Jane", "Mike", "Emily", "Rachel", "Jessica", "Louis", "Donna", "Katrina", "Alex"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    for _ in range(10):  # Create 10 directories
        # Generate a random name by combining a random first name and a random last name
        random_name = f"{random.choice(first_names)}_{random.choice(last_names)}"
        user_dir = os.path.join(base_dir, random_name)
        os.makedirs(user_dir, exist_ok=True)

    return HttpResponse("Users successfully created.")



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_images(request):
    base_dir = os.path.join(settings.MEDIA_ROOT, 'storage')
    responses = []

    for dir_name in os.listdir(base_dir):
        dir_path = os.path.join(base_dir, dir_name)
        if os.path.isdir(dir_path):
            image_path = os.path.join(dir_path, 'figma.jpg')
            if os.path.exists(image_path):
                base64_image = encode_image(image_path)
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
                }
                payload = {
                    "model": "gpt-4-vision-preview",
                    "messages": [{
                        "role": "user",
                        "content": [{
                            "type": "text",
                            "text": "rate this ux/ui?"
                        }, {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }]
                    }],
                    "max_tokens": 300
                }
                response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                if response.status_code == 200:
                    responses.append({"name": dir_name, "response": response.json()})

    return JsonResponse(responses, safe=False)