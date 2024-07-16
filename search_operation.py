import json
from pathlib import Path

# Load the JSON file
json_file = Path("video_ids.json")
with json_file.open("r") as file:
    json_list = json.load(file)

# The video ID you want to find
video_id = "oql3QUD2JyI"

for index, value in enumerate(json_list):
    if value == video_id:
        print(f"The video id {value} is found at {index}")
        break
else:
    print("Not found")