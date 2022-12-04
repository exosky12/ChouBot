############################################ IMPORTS #############################################

import requests
import shutil

############################################ ALL #################################################

videos = []
incrementation = 0

def generate_video_filename():
    global incrementation
    return "video/video"+str(incrementation)+".mp4"


def download_file(url):
    local_filename = generate_video_filename()
    with requests.get(url, stream=True) as r:
        with open(generate_video_filename(), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

############################################ CHANNELS ############################################

channels = ("UCCFqUJYKT97UerMmb6DM0bw", "UCo6Z9cEI8Hf3nyrLUfDITtA", "UCow2IGnug1l3Xazkrc5jM_Q", "UCAhaFPP6v3WCfK5Tjao0B7A", "UCWeg2Pkate69NFdBeuRFTAw", "UCNigJTVnMU8F3n08pYz0UYw")

channelsObject = {
    "Gotaga": channels[0],
    "Ixotag2": channels[1],
    "Joyca": channels[2],
    "Mastu": channels[3],
    "Squeezie": channels[4],
    "Amine": channels[5],
}

############################################ GET CHANNELS ID #####################################

# request = youtube.channels().list(
#     part = "statistics",
#     forUsername = "USER_NAME"
# )
# response = request.execute()

############################################ GET LASTEST VIDEO ###################################

for el in channels:
    lastest3Videos = requests.get("https://yt.lemnoslife.com/noKey/search?part=snippet&channelId=" + el + "&maxResults=3&order=date&type=video")
    response = lastest3Videos.json()
    getItemsSection = response.get("items")
    getOlderItem = getItemsSection[-1]
    getIDSection = getOlderItem.get("id")
    getVideoID = getIDSection.get("videoId")
    getUrl = "https://www.youtube.com/shorts/" + getVideoID
    getSnippetSection = getOlderItem.get("snippet")
    getTitle = getSnippetSection.get("title")
    videos.append({
        "id": getVideoID,
        "title": getTitle,
        "url": getUrl,
    })

############################################ GET MOST REPLAYED MOMENT ############################

# for video in videos:
#     getID = video.get('id')
#     mostReplayedRequest = requests.get("https://yt.lemnoslife.com/noKey/videos?part=mostReplayed&id=" + getID + "")
#     response = mostReplayedRequest.json()
#     getItemsSection = response.get("items")
#     mostReplayedSection = getItemsSection[0].get("mostReplayed")
#     getHeatMarkersDecorations = mostReplayedSection.get("heatMarkersDecorations")[0]
#     getTimedMarkerDecorationRenderer = getHeatMarkersDecorations.get("timedMarkerDecorationRenderer")
#     getStartMS = getTimedMarkerDecorationRenderer.get("visibleTimeRangeStartMillis")
#     getEndMS = getTimedMarkerDecorationRenderer.get("visibleTimeRangeEndMillis")
#     getStart = int(getStartMS / 1000) - 25
#     getEnd = int(getEndMS / 1000) + 25

############################################ DOWNLOAD MOMENT #####################################

incrementation = 0
for video in videos:
    idyt = videos[incrementation].get("id")
    result = requests.get("https://downloader.freemake.com/api/videoinfo/" + idyt)
    resultJson = result.json()
    getQualities = resultJson.get("qualities")[0]
    getUrl = getQualities.get("url")
    incrementation += 1
    download_file(getUrl)
