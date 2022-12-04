def generate_video_filename():
    global index
    return "video/video"+str(index)+".mp4"


def download_file(url):
    local_filename = generate_video_filename()
    with requests.get(url, stream=True) as r:
        with open(generate_video_filename(), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename
    
import requests
import shutil
import uuid

#############link de la video ou ID#################
link = "https://www.youtube.com/watch?v=jxgYR8s1eG8"
####################################################
index = 0
idyt = link.replace("https://www.youtube.com/watch?v=","")

for i in range(2):
    result = requests.get("https://downloader.freemake.com/api/videoinfo/" + idyt)
    resultJson = result.json()
    getQualities = resultJson.get("qualities")[0]
    getUrl = getQualities.get("url")
    index = index + 1
    download_file(getUrl)


