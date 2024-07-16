from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_keys = os.getenv("YOUTUBE_API")

#Build the YouTube Service
youtube = build("youtube", "v3", developerKey=api_keys)

Upload_ID = "UU3w193M5tYPJqF0Hi-7U-2g"

#Function to write the video ids into a JSON file
def get_playlist_details(maxResults,pageToken=None):
    request = youtube.playlistItems().list(
        part = "contentDetails",
        maxResults = maxResults,
        playlistId = Upload_ID,
        pageToken = pageToken
    )
    response = request.execute()    
    return response

playlist_details = get_playlist_details(50)

#Get the items and page token object
items = playlist_details["items"]
page_token = playlist_details["nextPageToken"]

#Store the video Ids into an list
video_ids = []
for item in items:
    video_id = item["contentDetails"]["videoId"]
    video_ids.append(video_id)

#Store all the 5243 video ids into the Video Ids list 
while page_token:
    playlist_details = get_playlist_details(50, page_token)
    items = playlist_details["items"]
    page_token = playlist_details.get("nextPageToken")
    for item in items:
        video_id = item["contentDetails"]["videoId"]
        video_ids.append(video_id)

#Write the video Ids into a JSON file
with open("video_ids.json", mode="w") as file:
    json.dump(video_ids, file, indent=4)

