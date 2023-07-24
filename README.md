# Wild Swimming
#### Video Demo: https://youtu.be/F7Oip6h9_sc
#### Description:

PLEASE NOTE: If trying the code you will need to input your own Googlemaps API key.
A few examples if you wish to test -
Input 1 - London
Input 2- Crouch End

Input 1 - Lake District
Input 2 - Great Langdale

Input 1 - Cornwall
Input 2 - Bossiney

The below locations are too far away from each other and will display a messaging say as much.
Input 1 - London
Input 2 - Bournemouth

Although currently living in the Sydney, I am from the UK where my partner loved to wild swim which gave me the idea for this project.

I began this project by requesting ChatGPT to provide a list of 125 wild swimming locations across the UK. To utilize this list effectively,
I developed a program that uses the Google Maps API to find the coordinates for each location and exports the information into a CSV file, organized by area, location name, latitude, and longitude.

The provided Python script is a program designed to help users find nearby swimming locations based on their current location.
It utilizes the Google Maps API to retrieve directions and distance information between the user's current location and various swimming spots.
The script requires users to input their Google Maps API key to access the necessary services.
Upon execution, the program prompts the user to enter two pieces of information: the location where they would like to swim and their current location,
these inputs are captured using the input() function in Python.

The main() function serves as the entry point of the script. It takes the user's swimming and current locations and proceeds to call other functions to fetch relevant data.
First, the current_location(m) function is called to obtain the geographical coordinates (latitude and longitude) of the user's current location.
It uses the Google Maps API's geocoding service to perform this task. If the entered location is invalid or not found, the script terminates with an error message.

Next, the check_areas() function is invoked to read a CSV file named "locations_with_coords.csv."
This file contains a list of swimming locations along with their corresponding geographical coordinates. The function parses the CSV data and stores the swimming locations in a list called swimming_areas.
The core functionality of the script lies within the distance_to_swim(current_location, swimming_locations) function.
This function calculates the driving distance and estimated time of travel between the user's current location and each swimming spot in the swimming_locations list.
To achieve this, it leverages the Google Maps API's directions service. The function then filters out swimming locations that can be reached within a 30-minute drive,
the relevant swimming locations, along with their names and Google Maps links, are stored in the output list.

Finally, the script displays the results to the user.
If there are swimming locations within a 30-minute driving distance, it prints the time required to reach each location, the name of the location, and a link to view the location on Google Maps.
On the other hand, if there are no swimming locations within the specified distance, the script informs the user with the message "No swimming locations within 30 minutes."

In conclusion, this Python script provides an interactive way for users to input their current location and the desired swimming location,
and it retrieves a list of nearby swimming spots within a 30-minute driving distance. By utilizing the Google Maps API, the program offers valuable information to those
seeking convenient and enjoyable places to swim.