import os
from dotenv import load_dotenv
import requests
from googleapiclient.discovery import build
import json

#load the environment variable
load_dotenv()

#Get the api key and build Youtube Service object
api_key = os.getenv("YOUTUBE_API")
youtube = build("youtube", "v3", developerKey=api_key)


def get_caption_list():
    request = youtube.captions().list(
        part = "snippet",
        videoId = "M7FIvfx5J10"
    )

    response_dict = request.execute()
    response_json = json.dumps(response_dict, indent=4)
    return (response_dict, response_json)

api_response = get_caption_list()
print(api_response[1])


