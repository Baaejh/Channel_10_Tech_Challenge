# Channel_10_Tech_Challenge
Submission for timed Technical Assessment @ channel 10

Overview:
After reading the challenge description for quite some time i was unsure of what exactly the question was asking (am i to query the API server and work with the returned CSV data, or was i suppost to create some sort of API type service that accepts requests in the form of CSV data and return a JSON response query ?) My understanding originally was that i could query the API, recieve CSV data, process the data and return the processed CSV data in JSON format.

NOTE: in my previous experiences developing i have only ever queried API services with JavaScript and have never worked with CSV formatting, Only JSON.

I decided that i would try and complete the challenge based on recieving a CSV type response from the API service, but realised that i could not seem to connect/recieve a response and or download anything CSV related (Error: 504 -> Screenshots attatched)

This lead to me only being able too succesfully recieve a JSON resposne from the API server, so i created a basic script that just query's the API server and returns the basic JSON data.

I decided to Improvise and decided to create another script that works on the sample CSV data that i was able to download from: "https://data.nsw.gov.au/data/dataset/nsw-covid-19-tests-by-location/resource/945c6204-272a-4cad-8e33-dde791f5059a"
the goal was to read in the CSV data by reading it in from the same directory the the Python Script is located within, just so i can work on formatting and working with the CSV formatted data.

I believe that there is a way that the CSV data can be queried via SQL possibly, but due to this being a new concept to me i did what i could to format the CSV data in python and returned a result that somewhat resembled the requested JSON format, i was able to generate a count for the dates of each test but did not have enough time to actually display the highest / Lowest counts.
