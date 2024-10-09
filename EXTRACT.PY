import json
import yt_dlp

URL = 'https://youtu.be/kfsKda_lNWs?si=AcDb5nxEf1ezK-Ii'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    with open('formdata.json','w') as f:
        json.dump(ydl.sanitize_info(info),f)