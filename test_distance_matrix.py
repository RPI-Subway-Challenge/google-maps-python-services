"""
This file focuses primarily on using the Distance Matrix API.
Refer to the link below for details and an overview of how it works.
https://developers.google.com/maps/documentation/distance-matrix/overview

"""
import requests     # Allows us to make HTTP requests to Google maps

"""
Given two addresses, computes the walking time between them.
The address should typically follow the parameter of:
    1313 Disneyland Dr, Anaheim, CA 92802
    [Street #] [Street Name], [City], [State Initials] [Zip Code]

    This includes spacing and comma, but slight variations in syntax
    should be acceptable in some cases.

@input:     addressA        - starting address
            addressB        - destination address
@output:    URL link to the JSON-formatted result
@return:    walking_time    - Time in minutes it takes to walk between the two addresses
"""
def address_walking_time(addressA, addressB):
    # Securely read the API key
    api_file = open("api-key.txt", "r")
    api_key = api_file.readline()
    api_file.close()

    # Starting address
    starting_point = addressA.replace(" ", "+")

    # Destination address
    destination_point = addressB.replace(" ", "+")

    # Base URL for accessing distance matrix API. Already set to walking directions
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&mode=walking&"
    url_test = url + "origins=" + starting_point + "&destinations=" + destination_point + "&key=" + api_key
    print(url_test)

    # Sends a Get request to Google Maps API server
    r = requests.get(url + "origins=" + starting_point + "&destinations=" +
                    destination_point + "&key=" + api_key)

    # return time as text and seconds
    walking_time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    # Print the time
    output_time(addressA, addressB, walking_time)

    return walking_time

"""
Given two stations, computes the walking time between them.
"""
def station_walking_time(stationA, stationB):
    # Securely read the API key
    api_file = open("api-key.txt", "r")
    api_key = api_file.readline()
    api_file.close()

    # Starting address
    starting_point = stationA + " station"
    starting_point = stationA.replace(" ", "+")

    # Destination address
    destination_point = stationB + " station"
    destination_point= stationB.replace(" ", "+")

    # Base URL for accessing distance matrix API. Already set to walking directions
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&mode=walking&"
    url_test = url + "origins=" + starting_point + "&destinations=" + destination_point + "&key=" + api_key
    print(url_test)

    # Sends a Get request to Google Maps API server
    r = requests.get(url + "origins=" + starting_point + "&destinations=" +
                    destination_point + "&key=" + api_key)

    # return time as text and seconds
    walking_time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    # Print the time
    output_time(stationA, stationB, walking_time)

    return walking_time

def output_time(origin, destination, time):
    print(origin + "   =====>   " + destination + "    " + time +"\n")

# Test cases
def main():
    ### ADDRESS TEST CASES ###
    address_walking_time_test_A = address_walking_time("1761 15th St, Troy, NY 12180",
                                                        "124 4th St, Troy, NY 12180")

    ### STATION TEST CASES ###
    station_walking_time_test_A = station_walking_time("Astor Pl",
                                                        "Canal St")

main()
