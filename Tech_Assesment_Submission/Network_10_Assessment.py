# Channel 10 Technical assessment Submission (Backend API Web Service Application)
# Created by: Bailey Hutchings

# Importing modules
import csv
import json
import io
from flask import Flask, request

# Flask application instance
flask_instance = Flask(__name__)


# Logic behind POST request Handler (Exposes '/Request' Endpoint )
@flask_instance.route('/', methods=['GET', 'POST'])
@flask_instance.route('/CSV_Request', methods=['GET', 'POST'])
def handle_POST_request():
    if request.method == 'POST':
        try:
            # Searches for 'CSV_data' Key within request body
            raw_request_data = request.files['CSV_data'] 

            if not raw_request_data:
                return "No file or data recieved... Try Again"

            # processes the clients request data
            return process_client_request(raw_request_data)

        except Exception as post_request_exception:
            print(post_request_exception)
            print('An error occoured Handling the request ... Try Again')
            return 'An error occoured Handling the request ... Try Again'

    elif request.method == 'GET':
        return 'GET Method Recieved, This API Endpoint will only Respond to POST Requests...'


# Method loops thru and extracts / aggreagtes the clients request data
def process_client_request(client_request):
    try:
        # Dictionary for storing the aggregated Data
        pre_aggregated_data = {}

        # Formats/decodes and prepares request data
        formatted_CSV = csv.DictReader(io.StringIO(client_request.stream.read().decode("UTF8"), newline=None))

        # loops thru formatted CSV data & extracts/aggregates the desired data
        for entry in formatted_CSV:
            if entry['lga_name19'] != "":
                lga_name = entry['lga_name19']
                test_date = entry['test_date']

                if lga_name in pre_aggregated_data.keys():
                    pre_aggregated_data[lga_name]['total_count'] += 1

                    if test_date in pre_aggregated_data[lga_name]['test_date_count'].keys():
                        pre_aggregated_data[lga_name]['test_date_count'][test_date] += 1
                    else:
                        pre_aggregated_data[lga_name]['test_date_count'][test_date] = 1
                else:
                    pre_aggregated_data[lga_name] = {}
                    pre_aggregated_data[lga_name]['lga_code'] = entry['lga_code19']
                    pre_aggregated_data[lga_name]['lga_name'] = lga_name
                    pre_aggregated_data[lga_name]['total_count'] = 1
                    pre_aggregated_data[lga_name]['greatest'] = {}
                    pre_aggregated_data[lga_name]['least'] = {}
                    pre_aggregated_data[lga_name]['test_date_count'] = {test_date: 1}

        # calls function to find greatest / least dates & update aggregated_data
        return aggregate_data(pre_aggregated_data)

    except Exception as process_request_exception:
        print(process_request_exception)
        print('An error occoured Handling the request ... Try Again')
        return 'An error occoured Handling the request ... Try Again'


# Handles the logic behind finsing the greatest/least test dates
def aggregate_data(request_data):
    aggregated_data = request_data
    finalised_data = []

    # *** GREATEST/LEAST LOGIC ***
        # loops through Keys and find the largest / smallest counts of each date
    for lga_name_key in aggregated_data.keys():
        greatest_template = {"count": 0, "date": ""}
        least_template = {"count": float('inf'), "date": ""}

        for date in aggregated_data[lga_name_key]['test_date_count'].keys():
            if aggregated_data[lga_name_key]['test_date_count'][date] > greatest_template['count']: 
                greatest_template['count'] = aggregated_data[lga_name_key]['test_date_count'][date]
                greatest_template['date'] = date

            if aggregated_data[lga_name_key]['test_date_count'][date] < least_template['count']:
                least_template['count'] = aggregated_data[lga_name_key]['test_date_count'][date] 
                least_template['date'] = date

        # filling the greatest / least dates and removing excess data
        aggregated_data[lga_name_key]['greatest'] = greatest_template
        aggregated_data[lga_name_key]['least'] = least_template
        aggregated_data[lga_name_key].pop('test_date_count')

    # *** SORTING BY 'total_count' LOGIC ***
        # Creates a list ordering the data by the 'total_count'
    total_count_SORTED = sorted(aggregated_data, key=lambda x: (aggregated_data[x]['total_count']), reverse = True)
    
    # fills the 'finalised_list' with the aggregated CSV Data - ordered by 'total_count'
    for location in total_count_SORTED:
        finalised_data.append(aggregated_data[location])

    # returning / calling function that converts 'finalised_data' into JSON format
    return return_JSON_object(finalised_data)


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
