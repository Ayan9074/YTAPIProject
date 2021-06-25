from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'key.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
catid = int(input("Please input the category id: "))
title = input("Enter Video Title: ")
desc = input("Enter desc: ")
tags = eval(input('enter tags as list: '))
request_body = {
    'snippet': {
        'categoryI': catid,
        'title': title,
        'description': desc,
        'tags': tags
    },
    'status': {
        'privacyStatus': 'public',
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('ytapitest.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

# Thumbnail usage turned off for now
#service.thumbnails().set(
#    videoId=response_upload.get('id'),
#    media_body=MediaFileUpload('thumbnail.png')
#).execute()
