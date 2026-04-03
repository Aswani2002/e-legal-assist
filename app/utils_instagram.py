import requests

RAPIDAPI_KEY = "fcffe94a9cmsn20b22391e824a94p152c39jsn4ad749cda721"
RAPIDAPI_HOST = "instagram-reels-downloader-api.p.rapidapi.com"

def get_instagram_mp4(insta_url):
    url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

    querystring = {"url": insta_url}

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    response = requests.get(url, headers=headers, params=querystring, timeout=10)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()

    if "video" not in data:
        raise Exception("No video found in API response")

    return data["video"]
