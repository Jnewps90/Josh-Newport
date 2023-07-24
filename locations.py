import csv
import googlemaps
import json

# Input your own google API key
gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')


def main():
    csv_data = get_locations()
    export_to_csv(csv_data)
    get_coords()

# Reorganise data and export to .txt file
def get_locations():
    organised_locations = []
    with open("locations.txt") as file:
        for line in file:
            new_line = line.strip().replace(" - ", ",")
            organised_locations.append(new_line.strip())


    return sorted(organised_locations)

# Read as dict and export to CSV
def export_to_csv(l):
    with open("locations.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["name", "area", "coordinates"])

        for location in l:
            writer.writerow([location])


def get_coords():
    locs_with_coords = []

    with open("locations.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if gmaps.geocode(row):
                geocode_result = gmaps.geocode(row)
                location = geocode_result[0]["geometry"]["location"]
                long = float(location["lng"])
                lat = float(location["lat"])
                name = row["name"].split(",")
                locs_with_coords.append({"area" : name[1],
                                         "name" : name[0],
                                         "lat" : [lat],
                                         "long" : [long]
                                         })

                locs_with_coords = sorted(locs_with_coords, key=lambda l: l["area"])

    with open("locations_with_coords.csv", "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["area", "name", "lat", "long"])
        writer.writeheader()
        writer.writerows(locs_with_coords)


if __name__ == "__main__":
    main()
