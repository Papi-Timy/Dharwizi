import math
import time
import json
import random
import datetime
from decimal import Decimal

import googlemaps
import collections

from requests import get

apiKey = "AIzaSyCa_lcyCRbSOMqRcnrv6WnlY1vVk1rrofY"
apiKey1 = "AIzaSyBx0n2ciqzWa6er_BjaDJvXZ6eYr1jKmN0"


#url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=New%20York%20City%2C%20NY&origins=Washington%2C%20DC&units=imperial&key=apiKey"

#Convert Seconds 
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

print(convert(3000))

gmaps = googlemaps.Client(key=apiKey)

#function using the data in the API
def get_distance_between_coords(origin, destination):
    # getting the current datetime
    now = datetime.datetime.now()

    # calling the function of the API
    ans = gmaps.directions(origin, destination, mode="driving", departure_time=now)

    # loading the data in a JSON file
    jsn = json.loads(json.dumps(ans))
    # returning the specific data found in Json > legs > distance > value
    # return distance and time
    return jsn[0]['legs'][0]['distance']['value'], jsn[0]['legs'][0]['duration']['value']


print(get_distance_between_coords("harare","bulawayo"))