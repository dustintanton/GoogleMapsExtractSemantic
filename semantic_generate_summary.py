import json
from datetime import datetime
from collections import defaultdict, Counter

filename = '2023_FEBRUARY.json'
start_date = datetime(2023, 2, 9)
end_date = datetime(2023, 2, 19, 23, 59, 59)

def parse_timestamp(timestamp_str):
    try:
        return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")

def meters_to_miles(meters):
    return meters / 1609.34

def summarize_trips(filename):
    with open(filename, 'rb') as file:
        raw_content = file.read()

    if raw_content.startswith(b'\xef\xbb\xbf'):  # UTF-8 BOM
        content = raw_content[3:].decode('utf-8-sig')
    else:
        content = raw_content.decode('utf-8', errors='ignore')

    data = json.loads(content)

    trips_by_date = defaultdict(list)
    last_place_name = None
    distance_by_transportation = Counter()

    for obj in data['timelineObjects']:
        if 'placeVisit' in obj:
            place_visit = obj['placeVisit']
            location = place_visit['location']
            place_name = location.get('name', location.get('address', 'Unknown Place'))
            last_place_name = place_name
        elif 'activitySegment' in obj:
            activity_segment = obj['activitySegment']
            start_time = parse_timestamp(activity_segment['duration']['startTimestamp'])
            end_time = parse_timestamp(activity_segment['duration']['endTimestamp'])
            
            if start_date <= start_time <= end_date:
                transit_method = activity_segment.get('activityType', 'Unknown Transit Method').replace('_', ' ').title()
                distance_miles = meters_to_miles(activity_segment.get('distance', 0))

                trips_by_date[start_time.date()].append({
                    'From': last_place_name or "Unknown Place",
                    'To': "Next Known Place",  # Placeholder, will be replaced later
                    'Transit Method': transit_method,
                    'StartTime': start_time.strftime("%H:%M"),
                    'EndTime': end_time.strftime("%H:%M"),
                    'Distance Travelled': f"{distance_miles:.2f} Miles"
                })

                # Tally the distance by transportation type
                distance_by_transportation[transit_method] += round(distance_miles, 2)

    # Replace placeholders with actual 'To' locations, which are the 'From' locations of the next trip
    for date, trips in trips_by_date.items():
        for i in range(len(trips) - 1):
            trips[i]['To'] = trips[i + 1]['From']
        if trips:
            trips[-1]['To'] = 'Unknown Place'

    return trips_by_date, distance_by_transportation

# Usage
trips_summary, total_distances = summarize_trips(filename)
for date in sorted(trips_summary):
    if start_date.date() <= date <= end_date.date():
        print(f"Trips for {date}:")
        for trip in trips_summary[date]:
            print(f"  From: {trip['From']} To: {trip['To']}")
            print(f"  Transit Method: {trip['Transit Method']}")
            print(f"  From {trip['StartTime']} to {trip['EndTime']}")
            print(f"  Distance Travelled: {trip['Distance Travelled']}\n")

print("Total distances travelled by transportation type:")
for transport, distance in total_distances.items():
    print(f"{transport}: {distance:.2f} Miles")