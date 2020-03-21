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
    q="surfing"
  )

  response = request.execute()
  r = json.dumps(response, indent=10)
  print(r)

  

if __name__ == '__main__':
    youtube_search()
 
