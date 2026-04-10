from datetime import date

import requests
API_KEY = 'AIzaSyBWtRn7IUzaVL4Jf2Mjef1GNeB8ZoHTmKE'

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key" :  API_KEY,
    'Content-Type': 'application/json'
}

while(True):
    user_input = input("Enter Prompt: ")
    if user_input.lower() == 'exit':
        break
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    print("Status:", response.status_code)

    data = response.json()
    print(data)

    if "candidates" in data:
        print(data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print("Error:", date)