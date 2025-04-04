# LinkedIn.py #

import requests

def linkedin(jobtitle, location="92000000"):

    print(" line 7 --  linkedin - jobtitle - > " , jobtitle )

    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs"

    querystring = {
        "keywords": jobtitle,
        "locationId": location,
        "datePosted": "anyTime",
        "sort": "mostRelevant"
    }

    headers = {
        "x-rapidapi-key": "5656a3ac67mshed8d74c7cccd299p11461cjsn869810802cac",
        # "x-rapidapi-key": "df9bb597aemsh341a16c30f8ed03p1db9c3jsn5878fc6ba75a",
	    "x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        json_data = response.json()
        jobs = json_data.get("data", [])[:5]

        print(" line 30 --  linkedin - jobs - > ", jobs)

        if not jobs:
            return f"❌ No jobs found for this title: {jobtitle}."

        result = []
        for job in jobs:
            title = job.get("title", "No title")
            link = job.get("url", "No URL")
            result.append(f"{title} - {link}")

        return "\n".join(result)

    except Exception as e:
        print("[LinkedIn ERROR]", e)
        return "⚠️ LinkedIn API error or no jobs available."

# LinkedIn.py #
