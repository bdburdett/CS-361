from flask import *
import json, time
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    
    now = datetime.now() 
    data_set = {'Timestamp': now.strftime("%m/%d/%Y, %H:%M:%S")}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)