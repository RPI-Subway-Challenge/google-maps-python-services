import requests     # Allows us to make HTTP requests to Google maps

# Securely read the API key
api_file = open("api-key.txt", "r")
api_key = api_file.readline()
api_file.close()

# Starting address
starting_point = "Disneyland"
starting_point = starting_point.replace(" ", "+")
# Destination address
destination_point = "Universal studios"
destination_point = destination_point.replace(" ", "+")

# Base URL for accessing distance matrix API
# Mode is already set to walking
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&mode=walking&"

# Get response
url_test = url + "origins=" + starting_point + "&destinations=" + destination_point + "&key=" + api_key

print(url_test)
r = requests.get(url + "origins=" + starting_point + "&destinations=" +
                 destination_point + "&key=" + api_key)

# return time as text and seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

# Print the travel time
print("\nThe total travel time from starting point to destination is", time)
