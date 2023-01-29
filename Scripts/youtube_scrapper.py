import requests
import json

BASE_URL = "https://www.youtube.com/youtubei/v1/search"

def getYtSearchJsonData(USER_QUERY):

    BODY_DATA = '{"context":{"client":{"clientName":"WEB","clientVersion":"2.20221220.09.00"}},"query":"' + USER_QUERY + '"}'

    response = requests.post(BASE_URL, data=BODY_DATA)

    json_response = json.loads(response.text)

    return json_response

QUERY = "Unholly"

JSON_SEARCH_DATA = getYtSearchJsonData(QUERY)

SEARCH_RESULTS = JSON_SEARCH_DATA["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]

VIDEOS_DATASET = []

for VIDEO_JSON in SEARCH_RESULTS:

    try:

        VIDEO_DATA = VIDEO_JSON["videoRenderer"]

        video_id = VIDEO_DATA["videoId"]

        video_title = VIDEO_DATA["title"]["runs"][0]["text"]

        video_length = VIDEO_DATA["lengthText"]["simpleText"]

        VIDEOS_DATASET.append({"id":video_id, "title":video_title, "length":video_length})

    except:

        pass


print(VIDEOS_DATASET)
print(len(VIDEOS_DATASET))
