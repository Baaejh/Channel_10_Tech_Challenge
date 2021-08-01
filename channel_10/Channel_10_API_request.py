# Channel 10 Covid information api connection

# Unable to connect to api server for CSV related data, so a standard Json response
# is recieved (Answer is continued/attemped in)

import urllib.request
import json

url = 'https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=945c6204-272a-4cad-8e33-dde791f5059a'

# Connecting to API service
with urllib.request.urlopen(url) as response:
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    
    # variable containing spi response data
    data_records = json_data['result']['records']

    #basic loop thru the json Data
    for item in data_records:
        print(item)
