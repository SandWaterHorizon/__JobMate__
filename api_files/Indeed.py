# indeed.py #


import requests


def indeed_job_search(job_query, country="de"):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query": job_query, "page": "1", "num_pages": "1", "country": country, "date_posted": "all"}

    headers = {
        "x-rapidapi-key": "68cf7760bcmshc2ce72230cf48cfp11c682jsnd8fc85c85fb9",
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    jobs = response.json()["data"][:5]
    result = []
    for job in jobs:
        title = job.get("job_title", "No title")
        link = job.get("job_apply_link", "No URL")
        result.append(f"{title} - {link}")

    return "\n".join(result)


# indeed.py #