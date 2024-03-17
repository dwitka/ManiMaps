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

### How To Run The App
**NOTE: You will need a Goggle Maps API Key to run the app!**
1. Create a local git repository.
    - Open up your terminal or command line interface.
    - Change into the directory where you want to clone the app.
    - Create a Folder named 'code' or whatever you want to call it.
    - Change into your 'code' directory.
    - Make sure git is installed.
    - In terminal run command:
```
$ git commit .
```
2. Clone the repository.
    - In terminal run command:
```
$ git clone https://github.com/dwitka/ManiMaps.git
```
3. Add your API_Key to the code:
   - Open the file app.py with a text editor.
   - Above the data line ADDRESSES = [] add the line: (Make sure your api key is in quotes.) ...and save.
```
API_KEY = 'my api key'
```
4. Run the app.
    - In terminal run command:
```
$ python3 app.py
```
5. You should see the ouput:
![Screenshot of the output using a CLI](output.png)
