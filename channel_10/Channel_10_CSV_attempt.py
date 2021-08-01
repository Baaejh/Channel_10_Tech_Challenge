# Channel 10 attempt at working with CSV files, 
# reads csv file in from local directory as API CSV requests were timing out

# Due to not getting around to properly sorting the greatest / smallest date counts
    # the CSV data used is from a smaller section of the test CSV file
    # the full size test CSV file cannot be copied to GitHub
    # The full size test file can be replaced

# Imports
import csv
import json

# CSV File large and smaller test file
filename_csv_test = 'sample_data_small.csv'

# dictionary containing data extrated from CSV File
dict_data = {}

# sorting data
def sort_csv_data(csv_file):

    with open(csv_file, 'r') as csv_file:
        # creating a csv reader object
        csv_read = csv.DictReader(csv_file)

        # extracting each row's data one by one and adding to dictionary
        for row in csv_read:
            if row['lga_name19'] != "":
                lga_name = row['lga_name19']
                current_date = row['test_date']

                if lga_name in dict_data.keys():
                    dict_data[lga_name]['total_count'] += 1

                    if current_date in dict_data[lga_name]['date_count'].keys():
                        dict_data[lga_name]['date_count'][current_date] += 1
                    else:
                        dict_data[lga_name]['date_count'][current_date] = 1


                else:
                    dict_data[lga_name] = {}
                    dict_data[lga_name]['lga_code'] = row['lga_code19']
                    dict_data[lga_name]['lga_name'] = lga_name
                    dict_data[lga_name]['total_count'] = 1
                    dict_data[lga_name]['date_count'] = {current_date: 1}



def display_csv_data(data):
    dictionary_data = data
    json_object = json.dumps(dictionary_data, indent = 4)

    return print(json_object)




# Calling Functions
sort_csv_data(filename_csv_test)

display_csv_data(dict_data)





