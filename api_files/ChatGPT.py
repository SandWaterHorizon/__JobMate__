# ChatGPT.py

import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def format_for_target_api(user_message: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": (
                "You are a helpful assistant that converts user requests into job-title as a JSON string "
                "with field: job_title."
            )},
            {"role": "user", "content": user_message}
        ]
    )

    message = response.choices[0].message['content']

    # Ensure valid JSON
    try:
        json.loads(message)
        return message
    except json.JSONDecodeError:
        return json.dumps({"job_title": "fullstack"})


# ChatGPT.py