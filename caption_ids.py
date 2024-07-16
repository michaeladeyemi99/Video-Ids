from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import json
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

#load the environment variable
load_dotenv()

#Get the api key and build Youtube Service object
api_key = os.getenv("YOUTUBE_API")
youtube = build("youtube", "v3", developerKey=api_key)

# Get the file path
json_file = Path("video_ids.json")
with json_file.open("r") as file:
    json_list = json.load(file)

#Function to get the Caption ID
def get_caption_id(video_id):
    request = youtube.captions().list(
        part = "snippet",
        videoId = video_id
    )
    response = request.execute()
    return response

items = []

#This is the video_id's index number it stopped at so it can continue from here
video_id_index = 202

#Append each item into a list called items... remember the item is also a list
for index,value in enumerate(json_list):
    if index >= video_id_index:
        try:
            snippet_captions = get_caption_id(value)
            logging.info(f"Snippet captions retrieved for video ID: {value}")
            item = snippet_captions.get("items",[])
            items.extend(item)
        except Exception as e:
            logging.error(f"""The API request failed at {value} : \n\n{e}\n\n""")
            if "quotaExceeded" in str(e):
                logging.error(f"The quota has been exceeded and you could check for {value}")
                break
        

#Append the caption id and language into a dictionary
caption_id_snippets = []
for item in items:
    try:
        caption_id = item["id"]
        snippet = item["snippet"]
        caption_id_snippet = {"id" : caption_id, "snippet" : snippet}
        caption_id_snippets.append(caption_id_snippet)
    except KeyError as e:
        logging.error(f"Missing expected key in item: {e}")

output_file = Path("caption_id_snippet.json")
with output_file.open(mode="w") as file:
    json.dump(caption_id_snippets, file, indent=4)
    logging.info("Json file created and written")

    





