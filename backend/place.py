import re; 

def strip_nonalphanumerical(string: str):
    return re.sub('[^a-zA-Z0-9 ]+', '', string, flags=re.UNICODE) 

class OpeningHours:
    def __init__(self, raw : dict):
        self.periods = list()
        for period_info in raw['periods']:
            self.periods.append(Period(period_info))
    
    def opened(self, weekday: int, time: int): 
        for period in self.periods:
            if (period.contains(weekday, time)):
                return True
        return False

class Period:
    def __init__ (self, raw: dict):
        self.open_time = int(raw['open']['time'])
        self.close_time = int(raw['close']['time'])
        self.open_day = int(raw['close']['day'])
        self.close_day = int(raw['close']['day'])
    
    def contains(self, weekday: int, time: int) -> bool:
        if (weekday == self.open_day):
            if (weekday == self.close_day):
                return self.open_time <= time and time <= self.close_time
            return self.open_time <= time
        if (weekday == self.close_day):
            return time <= self.close_time
        return False



class Place:
    def __init__(self, place_id: str, address: str = None, location: tuple = None, name: str = None, rating: float = None, 
                    time: OpeningHours = None, price_rating: int = None, categories: list = [], description: str = None):
        self.place_id = place_id
        self.address = address
        self.location = location
        self.name = name
        self.rating = rating
        self.open_hours = time
        self.price_rating = price_rating
        self.categories = categories
        self.desc = description

    def __str__(self):
        return self.name + " " + self.address
    def __repr__(self):
        return self.name + " " + self.address + "\n"

    def from_raw(self, raw: dict) -> None:
        self.address = raw["formatted_address"]
        self.place_id = raw['place_id']
        self.name = strip_nonalphanumerical(raw['name'])
        self.location = str(raw['geometry']['location']['lat']) + " " + str(raw['geometry']['location']['lng'])
        if ("current_opening_hours" in raw.keys()):
            self.open_hours = OpeningHours(raw["current_opening_hours"])
        
        if ("editorial_summary" in raw.keys()):
            self.desc = raw["editorial_summary"]["overview"]
        #elif ("reviews" in raw.keys()):
            #self.desc = raw["reviews"][0]["text"]
            #print(self.desc)
        else:
            print("missing summary: " + self.name)
            #print("insufficient reviews")
            self.desc=self.name

        if ("price_level" in raw.keys()):
            self.price_rating = int(raw["price_level"])
        else:
            self.price_rating = 0
            print("missing price level: " + self.name)
            pass

        if ("rating" in raw.keys()):
            self.rating = float(raw["rating"])
        else:
            print("missing rating: " + self.name)
            pass

        self.categories = raw["types"]
    
    

class Route:
    def __init__(self, place_a: Place, place_b: Place, raw: dict):
        self.place_a = place_a
        self.place_b = place_b
        self.route = list()
        self.total_dist = path['legs']['distance']['value']
        self.total_time = path['legs']['duration']['value']
        self.route.append(raw['legs']['steps']['start_location'])
        for path in raw['legs']['steps']:
            self.route.append(raw['legs']['steps']['end_location'])
