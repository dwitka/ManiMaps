# ManiMaps

### Project Description
ManiMaps is currently a working python application that uses the Google Maps API to extract distances between addresses. 
The app.py module reads a standard text file where each line consists of an address, it builds an http request and sends
it to google's servers. The app receives a json response which is then refined and structured. Access to the app is gained 
through a CLI.

Future versions will incorprate a TSP algorithm to calculate an optimal route.

The screenshot below shows the output of running the app through a CLI. 5 different addresses are used this produces 10 
results. For every line the output shows two addresses and the distance between them in meters.

### Output
![Screenshot of the output using a CLI](output.png)
