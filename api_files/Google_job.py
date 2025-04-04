import json
import requests
import os

from dotenv import load_dotenv
load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")

CACHE_FILE = "output.txt"

def indeed_job_search(job_query, country = "de"):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query":job_query,"page":"1","num_pages":"1","country": country,"date_posted":"all"}

    headers = {
        "x-rapidapi-key": "68cf7760bcmshc2ce72230cf48cfp11c682jsnd8fc85c85fb9",
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jobs = response.json()["data"][:5]
    result = []
    user_line = []
    with open("output.txt", "a") as f:
        f.write(f"\nnext search result\n{PHONE_NUMBER}\n{job_query}, {country}\n")
        for i, job in enumerate(jobs, 1):
            title = job.get("job_title", "No title")
            link = job.get("job_apply_link", "No URL")
            result.append(f"{i}. {title} - {link}")
            line = f"{i}. {title} - {link}\n"

            f.write(line)
            user_line.append(line)

    with open("user_saved_jobs.txt", "w") as f2:
        f2.write(str(user_line))



    return "\n".join(result)


