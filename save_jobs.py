# save_jobs #

import json
import os

FILE_NAME = "saved_jobs.json"
CACHE_FILE = "cache.json"

def save_number_line(number):
    if not os.path.exists(CACHE_FILE):
        return "⚠️ No job search history found. Search for jobs first!"

    with open(CACHE_FILE, "r") as file:
        try:
            jobs = json.load(file)
        except json.JSONDecodeError:
            return "⚠️ Error reading job cache."

    if number < 1 or number > len(jobs):
        return "⚠️ Invalid job number."

    job_description = f"{number} {jobs[number - 1]['job_title']} - {jobs[number - 1]['job_apply_link']}"

    if not os.path.exists(FILE_NAME):
        data = []
    else:
        with open(FILE_NAME, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

    if job_description in data:
        return "✅ Job already saved!"

    data.append(job_description)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    return f"✅ Job {number} saved successfully!"


def get_saved_jobs():
    if not os.path.exists(FILE_NAME):
        return ["❌ No saved jobs."]

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
            return data if data else ["❌ No saved jobs."]
        except json.JSONDecodeError:
            return ["⚠️ Error reading saved jobs."]

# save_jobs #