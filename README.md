

# **GoogleMapsExtractSemantic**
## Project Overview
"GoogleMapsExtractSemantic" is designed to extract location and transportation information from a JSON dump of your Google Timeline's Data. This tool is invaluable for individuals looking to analyze their movement patterns, transportation modes, and visited locations over time by leveraging data exported from Google Maps Timeline.

**Disclaimer: This project approximates location and transportation details based on available data. Due to limitations in the data and inference logic, the accuracy of the last known locations (e.g., destinations such as Airbnbs) and the precision of times/distances may vary. Some manual adjustments in the exported CSV might be necessary for complete accuracy.**

------------------

### Getting Your Google Timeline Data
To utilize this script, you first need to export your Google Timelines Data:

1. Visit Google Maps Timeline.
2. Click on the gear icon (⚙️) on the bottom right.
3. Choose to export either a single day's data or your entire history.
4. In the downloaded data, navigate to the "Location History (Timeline)" folder.
5. **Use the JSON files inside the "Semantic Location History" subfolder as input for this project.**
# Scripts and Their Variables
## generate_summary.py

**Description:** This script processes a specified JSON file containing Google Timeline data to compile and list trips. It extracts start and end locations, timestamps, and transportation methods for each trip based on the data provided.

**Functionality:**

  - Reads and decodes JSON data, accounting for potential byte order marks (BOM).
  - Parses each location entry to identify trips, marked by changes in place ID.
  - Extracts and prints details for each trip, including start and end locations (latitude and longitude), start and end times, and the transportation method used.

**Input:**

  - JSON file containing Google Timeline's location data in the format specified by Google, e.g., "February_9th_to_19th.json".

**Output:**

  - Console output listing each trip's details: starting and ending place IDs, transportation method, start and end times.
  
**Adjustable Variables:**

 - **filename** Specifies the input JSON file from which to pull data. The default is set to 'February_9th_to_19th.json'. Users should replace this with the name of their JSON file containing Google Timeline data.

**Usage Instructions:**

1. Ensure the desired JSON file is in the same directory as the script, or provide the relative or absolute path to the file.
2. Modify the filename variable in the script to match the name of your JSON file.
3. Run the script from your terminal or command prompt with Python:
```bash
python generate_summary.py
```
## Export_to_CSV.py
**Description:** This script is designed to aggregate and summarize trips data processed from a Google Timeline JSON file, then export the summarized information into a CSV file. The summarization includes compiling trips by date and calculating distances covered by different transportation methods.

**Functionality:**

 - Processes a specified JSON file to organize trip data by date.
 - Calculates the total distance covered for each transportation method used across all trips.
 - Exports the summarized data to a CSV file, which includes details like trip dates, places visited, and distances covered.

**Input:**

 - JSON file named 2023_FEBRUARY.json containing Google Timeline data.

**Output:**

 - CSV file named trip_summary.csv that includes summarized trip data.
 
**Adjustable Variables:**

 - **filename** The input JSON file from which to summarize data. The default is '2023_FEBRUARY.json'. This variable can be adjusted to match the filename of your data dump.

 - **csv_filename** Specifies the name of the output CSV file. Default is 'trip_summary.csv'.
start_date and end_date: These datetime objects define the range of dates for which to summarize trip data. Adjust these variables to match the period relevant to your data analysis.

**Usage Instructions:**

1. Place the JSON file you wish to 1. summarize in the same directory as the script, or specify the path to the file.
2. Update the filename, csv_filename, start_date, and end_date variables as necessary to reflect your data and desired output file name.
3. Run the script with Python to generate the CSV summary:
```bash
python Export_to_CSV.py
```


**Contributions and Feedback**
This project is open to contributions and improvements. If you encounter any issues or have suggestions for enhancements, please feel free to open an issue or submit a pull request. Don't expect a timely reply or solution.
