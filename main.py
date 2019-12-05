"""
This program uses the www.ns.nl website to automatically search for the time everybody needs to travel to the specific city.
"""

# imports
from selenium import webdriver
from contextlib import closing
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import Math

# function for parsing the results from the webpage
def parseResult(res):
    parsed = res[2:6]
    if parsed[-1] == "M":
        parsed = parsed[0:3]
    return int(parsed.split("H")[0]) * 60  + int(parsed.split("H")[1])


times = []
time = []

# locations of the 3 persons
locations = ["Middelburg", "Heerenveen", "Maastricht"]

# cities on the train map, possible target cities
cities = [
"Den Helder",
"Hoorn",
"Enkhuizen",
"Alkmaar",
"Beverwijk",
"Haarlem",
"Amsterdam Centraal",
"Amsterdam Amstel",
"Hilversum",
"Leeuwarden",
"Heerenveen",
"Steenwijk",
"Groningen",
"Assen",
"Zwolle",
"Enschede",
"Oldenzaal",
"Hengelo",
"Almelo",
"Maastricht",
"Heerlen",
"Geleen Oost",
"Sittard",
"Roermond",
"Weert",
"Venlo",
"Helmond",
"Eindhoven",
"Vlissingen",
"Middelburg",
"Goes",
"Kruiningen-Yerseke",
"Bergen op Zoom",
"Roosendal",
"Breda",
"Tilburg",
"'s-Hertogenbosch",
"Oss",
"Nijmegen",
"Arnhem",
"Dieren",
"Zutphen",
"Deventer",
"Apeldoom",
"Amersfoort",
"Utrecht Centraal",
"Ede-Wageningen",
"Driebergen-Zeist",
"Gouda",
"Dordrecht",
"Zandvoort aan Zee",
"Schiphol Airport",
"Amsterdam RAI",
"Leiden",
"Den Haag HS",
"Den Haag Centraal",
"Voorburg",
"Delft",
"Schagen,
"Rotterdam Centraal"
]

# for every combination of a city and a location:
for city in cities:
    time = []
    for location in locations:

        # starts a webbrowser which searches for the time. We use a special python module, since the ns.nl website is dynamic, so we need to use a function which not only waits for the page to load, but also to activate the dynamic features, which calculate the time.
        url = "https://www.ns.nl/en/journeyplanner/#/?vertrek=" + location + "&vertrektype=treinstation&aankomst=" + city + "&aankomsttype=treinstation&type=vertrek&tijd=2019-12-03T08:30&_requesttime=1574408283341"
        options = FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.get(url)
        page = browser.page_source
        html = BeautifulSoup(page, "lxml")
        divs = html.find("time", {"data-ng-attr-datetime": "{{ summaryCtrl.durationString }}"})
        try:
            #saving the time in an array
            time.append(parseResult(divs["datetime"]))
            print(location, " - " ,city, parseResult(divs["datetime"]))
        except:
            # catching errors which might appear due to bad network
            print(location, city, "Error")
            time.append(int(0))

        browser.quit()
    
    # calculating the total time for one city and adding it to the array
    time.append(time[0] + time[1] + time[2])
    print(time)
    times.append(time)
    print(city)

print(times)

# this algorithm finds the shortest time and ignores errors, so you may need to run this programm multiple times since the there might be an error in the connections to the best city.
best_time = 1000
for time in times:
    if time[3] < best_time & time[0] != 0 & time[1] != 0 & time[2] != 0 
        best_time = time[3]


# algorithm to find the least time difference for every train connection
least_difference = 1000
for time in times:
     if time[0] != 0 & time[1] != 0 & time[2] != 0 
        biggest_value = 0
        if Math.abs(time[0] - time[1]) > Math.abs(time[0] - time[2]):
            if Math.abs(time[1] - time[2]) > Math.abs(time[0] - time[2]):
                if Math.abs(time[0] - time[2]) < least_difference:
                    least_difference = Math.abs(time[0] - time[2])
            elif Math.abs(time[1] - time[2]) < least_difference:
                least_difference = Math.abs(time[1] - time[2])
        elif Math.abs(time[0] - time[1]) > Math.abs(time[1] - time[2]):
            if Math.abs(time[1] - time[2]) < least_difference:
                    least_difference = Math.abs(time[1] - time[2])
        elif Math.abs(time[0] - time[1]) < least_difference:
                    least_difference = Math.abs(time[0] - time[1])
        


