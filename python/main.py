from selenium import webdriver
from contextlib import closing
from bs4 import BeautifulSoup
url = "https://www.ns.nl/en/journeyplanner/#/?vertrek=Middelburg&vertrektype=treinstation&aankomst=Utrecht&aankomsttype=treinstation&type=vertrek&tijd=2019-12-03T08:30&_requesttime=1574408283341"
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def parseResult(res):
    parsed = res[2:6]
    if parsed[-1] == "M":
        parsed = parsed[0:3]
    return int(parsed.split("H")[0]) * 60  + int(parsed.split("H")[1])
times = []
time = []
locations = ["Middelburg", "Heerenveen", "Maastricht"]
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
"Rotterdam Centraal"
]

for city in cities:
    time = []
    for location in locations:
        url = "https://www.ns.nl/en/journeyplanner/#/?vertrek=" + location + "&vertrektype=treinstation&aankomst=" + city + "&aankomsttype=treinstation&type=vertrek&tijd=2019-12-03T08:30&_requesttime=1574408283341"
        options = FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.get(url)
        page = browser.page_source
        html = BeautifulSoup(page, "lxml")
        divs = html.find("time", {"data-ng-attr-datetime": "{{ summaryCtrl.durationString }}"}) #, {"class":"content"}) #travelTime_transfer--travelTime"})
        try:
            time.append(parseResult(divs["datetime"]))
            print(location, " - " ,city, parseResult(divs["datetime"]))
        except:
            print(location, city, "Error")
            time.append(int(0))

        browser.quit()
    time.append(time[0] + time[1] + time[2])
    print(time)
    times.append(time)
    print(city)

print(times)

