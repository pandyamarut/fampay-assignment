import json
from googleapiclient.discovery import build
# service = build('youtube', 'v3', developerKey='AIzaSyByoCAdqbcysrN665WGZI-EsL_MRhncLAY')

DEVELOPER_KEY = 'AIzaSyByoCAdqbcysrN665WGZI-EsL_MRhncLAY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  request= youtube.search().list(
    part="snippet",
    maxResults=25,
    type="video",
    q="cricket",
    order="date",
    publishedAfter="2020-01-12T23:20:50.52Z"
  )

  response = request.execute()
  r = json.dumps(response, indent=5)
  print(r)

  

if __name__ == '__main__':
    youtube_search()
 
