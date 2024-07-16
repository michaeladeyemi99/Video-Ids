from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load the environment variables from a .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("YOUTUBE_API")

# Build YouTube service
youtube = build("youtube", "v3", developerKey=api_key)

# Get the upload ID using the handle
def get_upload_id():
    request = youtube.channels().list(
        part="contentDetails",
        forHandle="@Drberg"
    )
    response = request.execute()
    return response

upload_id_details = get_upload_id()

if "items" in upload_id_details and len(upload_id_details["items"]) != 0:
    upload_id = upload_id_details["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    print(f"Upload ID: {upload_id}")
else:
    print("No upload found with the given handle.")

Upload_ID = "UU3w193M5tYPJqF0Hi-7U-2g"

