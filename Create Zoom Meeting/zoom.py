
import jwt
import requests
import json
from time import time


# Enter your API key and your API secret
API_KEY = 'Your_Api_Key'
API_SEC = 'Your_Api_Secret_Key'


# This will genrate a JWT token for you

def generateToken():
    token = jwt.encode(

        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 1000},

        # Secret used to generate token signature
        API_SEC,

        # Specify the hashing alg
        algorithm='HS256'
    )
    return token.decode('utf-8')


# create json data for post requests
meetingdetails = {"topic": "Welcome to Zoom",
                  "type": 2,
                  "start_time": "2022-01-22T10: 11: 00",
                  "duration": "45",
                  "timezone": "India/Delhi",
                  "agenda": "test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "True",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }


# JWT are passed via headers which takes key value pair

def createMeeting():
    headers = {'Authorization': 'Bearer ' + generateToken(),
               'Content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
    print(y)

    # Record the meet details in file

    f = open("details.txt","w")
    f.write(f'Topic of meeting is: {meetingdetails["topic"]}\n')
    f.write(f'Meet start timing is: {meetingdetails["start_time"]}\n')
    f.write(f'Joining URL is: {join_URL}\n')
    f.write(f'Joining Password is: {meetingPassword}\n')
    print(
        f'\n here is your zoom meeting link {join_URL} and your password: "{meetingPassword}"\n')


# run the create meeting function
createMeeting()

