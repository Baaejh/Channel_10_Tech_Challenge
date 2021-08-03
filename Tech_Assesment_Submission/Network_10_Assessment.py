# Channel 10 Technical assessment Submission (Backend API Web Service Application)
# Created by: Bailey Hutchings

# Importing modules
import csv
import json
import io
from flask import Flask, request

# Flask application instance
flask_instance = Flask(__name__)

# dictionary containing aggregated data from client request
aggregated_data = {}


# Logic behind POST request Handler (Exposes '/Request' Endpoint )
@flask_instance.route('/CSV_Request', methods=['POST'])
def handle_POST_request():
    if request.method == 'POST':
        try:
            # Searches for 'CSV_data' Key within request body
            raw_request_data = request.files['CSV_data'] 

            if not raw_request_data:
                return "No file or data recieved... Try Again"

            # processes the clients request data
            process_client_request(raw_request_data)

            # returns aggregated / formatted data
            return return_JSON_object(aggregated_data)

        except Exception as post_request_exception:
            print('An error occoured Handling the request ... Try Again')
            print(post_request_exception)
            return 'An error occoured Handling the request ... Try Again'


# Method loops thru and extracts / aggreagtes the clients request data
def process_client_request(client_request):
    try:
        # Formats/decodes and prepares request data
        formatted_CSV = csv.DictReader(io.StringIO(client_request.stream.read().decode("UTF8"), newline=None))

        # loops thru formatted CSV data & extracts/aggregates the desired data
        for entry in formatted_CSV:
            if entry['lga_name19'] != "":
                lga_name = entry['lga_name19']
                test_date = entry['test_date']

                if lga_name in aggregated_data.keys():
                    aggregated_data[lga_name]['total_count'] += 1

                    if test_date in aggregated_data[lga_name]['test_date_count'].keys():
                        aggregated_data[lga_name]['test_date_count'][test_date] += 1
                    else:
                        aggregated_data[lga_name]['test_date_count'][test_date] = 1
                else:
                    aggregated_data[lga_name] = {}
                    aggregated_data[lga_name]['lga_code'] = entry['lga_code19']
                    aggregated_data[lga_name]['lga_name'] = lga_name
                    aggregated_data[lga_name]['total_count'] = 1
                    aggregated_data[lga_name]['greatest'] = {}
                    aggregated_data[lga_name]['least'] = {}
                    aggregated_data[lga_name]['test_date_count'] = {test_date: 1}

        # calls function to find greatest / least dates & update aggregated_data
        aggregate_dates(aggregated_data)

    except Exception as process_request_exception:
        print(process_request_exception)
        return print('An error occoured Handling the request ... Try Again')

# Handles the logic behind finsing the greatest/least test dates
def aggregate_dates(request_data):
    for lga_name_key in request_data.keys():
        greatest_template = {"count": 0, "date": ""}
        least_template = {"count": float('inf'), "date": ""}

        for date in request_data[lga_name_key]['test_date_count']:
            if request_data[lga_name_key]['test_date_count'][date] > greatest_template['count']: 
                greatest_template['count'] = request_data[lga_name_key]['test_date_count'][date]
                greatest_template['date'] = date

            if request_data[lga_name_key]['test_date_count'][date] < least_template['count']:
                least_template['count'] = request_data[lga_name_key]['test_date_count'][date] 
                least_template['date'] = date

        aggregated_data[lga_name_key]['greatest'] = greatest_template
        aggregated_data[lga_name_key]['least'] = least_template
        aggregated_data[lga_name_key].pop('test_date_count')     


# converts data into a JSON object
def return_JSON_object(req_data):
    try:
        json_object = json.dumps(req_data, indent = 4)
        return json_object
    except Exception as return_JSON_exception:
        print(return_JSON_exception)
        print('There was an error Returning the JSON object ... Try Again')
        return 'There was an error Returning the JSON object ... Try Again'


# Main application Start
if __name__ == '__main__':
    # Start flask instance (localhost, port: 8000)
        # NOTE: if port is in use update port parameter below
    flask_instance.run(host='127.0.0.1', port=8000)
 
    
     




