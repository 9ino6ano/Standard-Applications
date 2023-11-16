#Find the distance between 2 locations either two cities, countries or continents
#Geopy makes it easy for python developers to locate the coordinates of addresses,cities,countries and landmarks across the globe
#To confirm the distance, use this website
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa09tWWhyRU5LbWNjV1lMLVk1VDA3dUxIWEg3Z3xBQ3Jtc0trR2FzejFwc010c1dySHJvNVBRT3lJODd3bk1UTG1MX2NRRElDVGdHQzlMLVVab3NZenduZUs1QkVibTJlZW9xSlBSNlBaMk51LW9FVlpxNjRnYl8taS1wYTROMVcwQnE2ZVRicjZ1aDJYQk1uZEhfcw&q=https%3A%2F%2Fwww.geodatasource.com%2Fdistance-calculator&v=7JJRT65_PEI
from geopy.distance import geodesic

#loading the latitude and longitude from two places
first_place=(52.2296756,21.0122287)
second_place=(52.406374,16.9251681)

#print distance in km
distance=int(geodesic(first_place,second_place).km)
print(distance,"Kilometer")