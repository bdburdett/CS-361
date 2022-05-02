import requests
import json

class Time:
    def get_time(self):
        response_API = requests.get('http://15ba-2603-9001-5504-e427-ed89-6eda-e851-bb6.ngrok.io')

        data = response_API.text
        parse_json = json.loads(data)
        active_case = parse_json['Timestamp']
        print("The date is:", active_case)


time = Time()

time.get_time()