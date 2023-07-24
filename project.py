import sys
import googlemaps
import csv
from datetime import datetime

# Input your own google API key
gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')


def main():
    swim = input("Where would you like to swim? ")
    where_are_you = input("Where are you now? ")
    current = current_location(where_are_you)
    swimming_locations = check_areas()
    output = distance_to_swim(current, swimming_locations)
    if not output:
        print("No swimming locations within 30 mintues")
    else:
        print(*output, sep="\n")

# Get coords of current location
def current_location(m):
    geocode_result = gmaps.geocode(m)
    try:
        location = geocode_result[0]["geometry"]["location"]
        return location

    except IndexError:
        sys.exit("Please enter a city, town or village")
# Check list of swimming areas in CSV
def check_areas():
    swimming_areas = []

    with open("locations_with_coords.csv") as file:
        reader = csv.DictReader(file)
        for coords in reader:
            destination = coords
            swimming_areas.append(destination)
    return swimming_areas

# Return swimming locations within 30 minutes
def distance_to_swim(current_location, swimming_locations):
    now = datetime.now()
    output = []
    for i in swimming_locations:
        name = i["name"]
        lat = i["lat"].replace("[", "").replace("]", "")
        long = i["long"].replace("[", "").replace("]", "")
        swimming = f"{lat}, {long}"

        directions_result = gmaps.directions(current_location, swimming, mode="driving", departure_time=now)
        link = f"https://www.google.com/maps/search/?api=1&query={lat},{long}"

        try:
            for step in directions_result[0]["legs"]:
                duration_text = step["duration"]
                time = duration_text["text"]
                time_split = time.split()

                if int(time_split[0]) <= 30 and time_split[1] == "mins":
                    printed_output = f"{time}, {name}, {link}"
                    output.append(printed_output)

        except IndexError:
            pass
    return output

if __name__ == "__main__":
    main()