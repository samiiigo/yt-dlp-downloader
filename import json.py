import json

with open('video_info.json') as f:
    curinfo = json.load(f)

    print(curinfo['thumbnails'][4])
    #if curinfo['thumbnails']["resolution"] == "196x110":
    #    print(curinfo['thumbnails']["url"])