# Network_10_Tech_Challenge
Submission for the Network 10 Junior Developer technical Assessment


**About:** 

This Application Exposes a REST API endpoint via a localhost connection, the application will accept client HTTP POST requests in a CSV format, the CSV data is aggregated and returned back to the client in JSON format.

The 'Tech_Assessment_Submission' folder on the main branch Contains the Applications Source code [Network_10
_Assessment.py] and a small sample set of CSV data [sample_data_small.csv] in the required format.

The CSV data that is used/tested by this API Application endpoint can be downloaded from:
  - https://data.nsw.gov.au/data/dataset/60616720-3c60-4c52-b499-751f31e3b132/resource/945c6204-272a-4cad-8e33-dde791f5059a/download/pcr_testing_table1_location.csv



**Requirements:**

This Application is developed in Python (v3.9) and also relies on the 'Flask' (v2.0.1) web framework for handling and processing client 'POST' requests. The HTTP POST requests used for testing this API endpoint were conducted via 'Postman'. 

The following list contains the entire list of modules & softwares required for this application:
  
```
* Python - (This Application was created with v3.9)
* Flask Web Framework - (This Application was created with v2.0.1)
* Python Modules: [flask, csv, json, io]
```


**Setup [Host / Port]:**

This API application is designed to work via a localhost connection, the flask instance listens on the following host/port:
```
- HOST: 127.0.0.1
- PORT: 8000
(NOTE: if the selected port of 8000 is in use the port No. can be updated within the source code)
```


**Setup [HTTP POST Request]:**

The client must access the API at the following endpoints:
```
Endpoint_1: http://127.0.0.1:8000/
Endpoint 2: http://127.0.0.1:8000/CSV_Request
```

The client requests body must also contain the following information/data
```
POST Request type: 'form-data'
KEY: 'CSV_data'
VALUE: RAW CSV DATA / CSV File

```
**NOTE: The 'setup' folder contains an image of the postman HTTP Request settings**


**Using this Application:**

After the required softwares/technologies mentioned above are installed and ready to go, the user must ensure that the Python File --> (Network_10_Assessment.py) is running, ensuring that the application is actively listening/accepting requests at the desired address/port - [http://127.0.0.1:8000/]  OR  [http://127.0.0.1:8000/CSV_Request].

Once the Python script has been executed, and is actively accepting connections, the HTTP POST request containing the .CSV data may be made to the localhost address mentioned above, the desired JSON response should then be returned to the client that made the request.

