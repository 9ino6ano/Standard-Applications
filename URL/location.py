import geocoder

g=geocoder.ip("me")

print("Your Latitude and Longitude is: ",g.latlng)
