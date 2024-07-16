import io
import os
import logging

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError

# Setup logging
logging.basicConfig(level=logging.INFO)

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def caption_downloads():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    # Get credentials and create API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_local_server(port=8080)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )
#my id = AUieDabdceNoHzArA9DURjnugYB3Y0opUHT9WKr1Ym3X
#dr berg id = AUieDabkrgfnBlFC0-TxHdBZCTUw04DbcJScF5wmNAB1YwcJ5Iw
    try:
        request = youtube.captions().download(
            id="AUieDabkrgfnBlFC0-TxHdBZCTUw04DbcJScF5wmNAB1YwcJ5Iw",
            tfmt="srt"
        )

        fh = io.FileIO("srt_file.srt", "wb")
        download = MediaIoBaseDownload(fh, request)
        complete = False
        while not complete:
            status, complete = download.next_chunk()
            if status:
                logging.info(f"Download {int(status.progress() * 100)}%.")
    except HttpError as e:
        logging.error(f"An error occurred: {e}")
        if e.resp.status == 403:
            logging.error("403 Forbidden: The permissions associated with the request are not sufficient to download the caption track.")
            logging.error("Possible reasons:")
            logging.error("- The request might not be properly authorized.")
            logging.error("- The video owner might not have enabled third-party contributions for this caption.")
        raise

if __name__ == "__main__":
    caption_downloads()


