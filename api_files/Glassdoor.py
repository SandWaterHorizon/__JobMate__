# Glassdoor.py #

import requests

def glassdoor(jobtitle, location="92000000"):

    print(" line 8 -- in glassdoor py jobtitle ---- " , jobtitle )

    url = "https://glassdoor-real-time.p.rapidapi.com/companies/interview-details"

    querystring = {
        "keywords": jobtitle,
        "locationId": location,
        "datePosted": "anyTime",
        "sort": "mostRelevant"
    }

    headers = {
        "x-rapidapi-key": "4a150aa428msh09e7d1de77b4d40p1dd6adjsn40e85cb6267d",
        "x-rapidapi-host": "glassdoor-real-time.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()
        jobs = json_data.get("data", [])[:5]

        if not jobs:
            return "❌ No jobs found for this title."

        result = []
        for job in jobs:
            title = job.get("title", "No title")
            link = job.get("url", "No URL")
            result.append(f"{title} - {link}")

        return "\n".join(result)

    except Exception as e:
        print("[Glassdoor ERROR]", e)
        return "⚠️ Glassdoor API error or no jobs available."


if __name__ == "__main__":
    print(glassdoor("python"))

# Glassdoor.py #