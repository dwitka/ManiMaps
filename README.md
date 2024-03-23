# ManiMaps

### Project Description
ManiMaps is currently a working python application that uses the Google Maps API to extract data. Access to the app is gained 
through a CLI.

The ***distance.py*** module extracts distances between addresses. It reads a standard text file where each line consists of an address, 
it builds an http request and sends it to google's servers. The app receives a json response which is then refined and structured.

The ***geocode.py*** module returns a list of the longitude/latitude coordinates for addresses given.

Future versions will incorprate a TSP algorithm to calculate an optimal route.

The screenshot below shows the output of running ***distance.py*** through a CLI. 5 different addresses are used, this produces 10 
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
3. Confirm that there is a new folder named ManiMaps in your current directory.
    - Run the command:
    - ```$ ls```
4. Change into the ManiMaps folder.
    - Run the command:
    - ```$ cd ManiMaps```
5. Add your API_Key to the code:
   - Open the file app.py with a text editor.
   - Above the data line:
   - ```ADDRESSES = []```
   - Add the line:
   - ```API_KEY = 'my api key'```
   - Make sure your api key is in quotes.
   - Save the file.
6. Run the app.
    - In terminal run command:
```
$ python3 distance.py
```
7. You should see the ouput:
![Screenshot of the output using a CLI](output.png)
