# task 1

from geopy.distance import geodesic, great_circle
from geopy.geocoders import Nominatim
import webbrowser
from KruskulALgo import Graph

'''
1.	Get and mark locations of 5- 10 cities in Malaysia 
'''
geolocator = Nominatim()

cities = ["Kuala Lumpur", "Bayan Lepas", "Johor Bahru", "Kuala Terengganu", "Ipoh"]
locationDictionary = {}

print("loading latitude and longitude of the five cities we want into a dictionary")
for i in cities:
    location = geolocator.geocode(i)
    lat = location.latitude
    lang = location.longitude
    print(str((lat, lang)) + "---> " + i)
    locationDictionary.__setitem__(i, (lat, lang))

# task 2

print("")
# print("get locstion of the city from the dictionary")
# print(locationDictionary.get("Kuala Lumpur"))
# print("")
print("distances")

disArr = []
machingArr = []
resultsDictionary = {}
g = Graph(5)

for i in range(len(cities)):
    for l in range(len(cities)):
        if (cities[i] != cities[l]):
            dis = int(great_circle(locationDictionary.get(cities[i]), locationDictionary.get(cities[l])).km)
            # if (not disArr.__contains__(dis)):
            if (not machingArr.__contains__([cities[i], cities[l]])):
                disArr.append(dis)
                arrstomach = [cities[l], cities[i]]
                machingArr.append(arrstomach)
                g.addEdge(cities.index(arrstomach[0]), cities.index(arrstomach[1]), dis)
                # resultsDictionary.__setitem__(dis,arrstomach)
                print(str(dis) + " ---> " + cities[i] + " to " + cities[l])

# task 3
print("\n")
print("MST\n")

resutl = g.KruskalMST()

print(resutl)

print('\nMST success\n')

# task 4
bef = "var flightPlanCoordinates = ["
bef += '{lat: 3.1390, lng: 101.6869},{lat: 5.4163, lng: 100.3328},{lat: 3.1390, lng: 101.6869},{lat: 5.4163, lng: 100.3328},{lat: 4.5921, lng: 101.0901},{lat: 3.1390, lng: 101.6869},{lat: 4.5921, lng: 101.0901},{lat: 5.3117, lng: 103.1324},{lat: 5.4163, lng: 100.3328},{lat: 3.1390, lng: 101.6869},{lat: 5.3117, lng: 103.1324},{lat: 1.4927, lng: 103.7414},{lat: 5.4163, lng: 100.3328},{lat: 3.1390, lng: 101.6869},{lat: 1.4927, lng: 103.7414},{lat: 4.5921, lng: 101.0901},'
bef += "];"

loc = ""
loc += "var flightPlanCoordinates = ["
# add all locations here like "{lat: 3.1390, lng: 101.6869},"ies with their connections without MST Yet
# adding all cit

for res in resutl:
    FirstCityCordinates = locationDictionary.__getitem__(cities[res[0]])
    SecondCityCordinates = locationDictionary.__getitem__(cities[res[1]])

    fcityLat = str(FirstCityCordinates[0])
    fcityLang = str(FirstCityCordinates[1])

    scityLat = str(SecondCityCordinates[0])
    scityLang = str(SecondCityCordinates[1])

    loc += "{lat:" + fcityLat + ", lng:" + fcityLang + "},"
    if (resutl.index(res) == (len(resutl) - 3)):
        print("nothing")
        # loc += "{lat:" + scityLat + ", lng:" + scityLang + "}"
    else:
        loc += "{lat:" + scityLat + ", lng:" + scityLang + "},"

    print("added (" + cities[res[0]] + " --> " + cities[res[1]] + ") ditance is : " + str(res[2]) + "km")

loc += "];"

# {lat: -25.363, lng: 131.044};
marks = ""
for i in cities:
    locat = locationDictionary.get(i)
    marks += 'addMarker(' + '{lat: ' + str(locat[0]) + ',' + 'lng: ' + str(
        locat[1]) + '}' + ',' + '\'' + i + '\'' + ' , map);\n'

print(marks)
print(loc)

messageBef = '''<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>BeforeMST</title>
    <style>
        /* Always set the map height explicitly to define the size of the div
         * element that contains the map. */
        #map {
            height: 100%;
        }

        /* Optional: Makes the sample page fill the window. */
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAJdptlczUdaDZt77tH5WvdGjBfkC1zjTI&callback=initMap"></script>
    <script>
        // In the following example, markers appear when the user clicks on the map.
        // Each marker is labeled with a single alphabetical character.

        function initialize() {

            var bangalore = {lat: 12.97, lng: 77.59};

            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: {lat: 3.1546872, lng: 101.7136362},
                mapTypeId: 'terrain'
            });

            // This event listener calls addMarker() when the map is clicked.
            google.maps.event.addListener(map, 'click', function (event) {
                addMarker(event.latLng, map);
            });


            ''' + bef + '''

            var flightPath = new google.maps.Polyline({
                path: flightPlanCoordinates,
                geodesic: true,
                strokeColor: '#FF0000',
                strokeOpacity: 1.0,
                strokeWeight: 2
            });

            // Add a marker at the center of the map.
            //addMarker(bangalore, 'kuala', map);
            
            ''' + marks + '''
            
            //adding paths
            flightPath.setMap(map);
        }

        // Adds a marker to the map.
        function addMarker(location, city, map) {
            // Add the marker at the clicked location, and add the next-available label
            // from the array of alphabetical characters.
            var marker = new google.maps.Marker({
                position: location,
                label: city,
                map: map
            });
        }

        google.maps.event.addDomListener(window, 'load', initialize);
    </script>
</head>
<body>
<div id="map"></div>
</body>
</html>'''

messageAfT = '''<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>AfterMST</title>
    <style>
        /* Always set the map height explicitly to define the size of the div
         * element that contains the map. */
        #map {
            height: 100%;
        }

        /* Optional: Makes the sample page fill the window. */
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAJdptlczUdaDZt77tH5WvdGjBfkC1zjTI&callback=initMap"></script>
    <script>
        // In the following example, markers appear when the user clicks on the map.
        // Each marker is labeled with a single alphabetical character.

        function initialize() {

            var bangalore = {lat: 12.97, lng: 77.59};

            var map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: {lat: 3.1546872, lng: 101.7136362},
                mapTypeId: 'terrain'
            });

            // This event listener calls addMarker() when the map is clicked.
            google.maps.event.addListener(map, 'click', function (event) {
                addMarker(event.latLng, map);
            });


            ''' + loc + '''

            var flightPath = new google.maps.Polyline({
                path: flightPlanCoordinates,
                geodesic: true,
                strokeColor: '#FF0000',
                strokeOpacity: 1.0,
                strokeWeight: 2
            });

            // Add a marker at the center of the map.
            //addMarker(bangalore, 'kuala', map);

            ''' + marks + '''

            //adding paths
            flightPath.setMap(map);
        }

        // Adds a marker to the map.
        function addMarker(location, city, map) {
            // Add the marker at the clicked location, and add the next-available label
            // from the array of alphabetical characters.
            var marker = new google.maps.Marker({
                position: location,
                label: city,
                map: map
            });
        }

        google.maps.event.addDomListener(window, 'load', initialize);
    </script>
</head>
<body>
<div id="map"></div>
</body>
</html>'''

f = open('BeforeMST.html', 'w')
f.write(messageBef)
f.close()

f = open('AfterMST.html', 'w')
f.write(messageAfT)
f.close()

webbrowser.open('http://localhost:63342/MST/BeforeMST.html?_ijt=c7ngkfr16vghboir6k4utbl4sn')
webbrowser.open('http://localhost:63342/MST/AfterMST.html?_ijt=c7ngkfr16vghboir6k4utbl4sn')
