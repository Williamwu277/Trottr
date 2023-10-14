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
    def __init__(self, place_id: str, address: str = None, name: str = None, rating: float = None, 
                    time: OpeningHours = None, price_rating: int = None, categories: list = [], description: str = None):
        self.place_id = place_id
        self.address = address
        self.name = name
        self.rating = rating
        self.open_hours = time
        self.price_rating = price_rating
        self.categories = categories
        self.desc = description

    def from_raw(self, raw: dict) -> None:
        #self.address = raw[""]
        self.place_id = raw['place_id']
        self.name = raw["name"]
        if ("current_opening_hours" in raw.keys()):
            self.open_hours = OpeningHours(raw["current_opening_hours"])
        
        if ("editorial_summary" in raw.keys()):
            self.desc = raw["editorial_summary"]
        elif ("reviews" in raw.keys()):
            print("summray not found, trying reviews: " + self.name)
            self.desc = raw["reviews"][0]["text"]
            print(self.desc)
        else:
            print("insufficient reviews")

        if ("price_level" in raw.keys()):
            self.price_rating = int(raw["price_level"])
        else:
            print("missing price level: " + self.name)

        if ("rating" in raw.keys()):
            self.rating = float(raw["rating"])
        else:
            print("missing rating: " + self.name)

        self.categories = raw["types"]

class Route:
    def __init__(self, place_a: Place, place_b: Place, raw: dict):
        this.place_a = place_a
        this.place_b = place_b
        this.route = list()
        this.total_dist = path['legs']['distance']['value']
        this.total_time = path['legs']['duration']['value']
        this.route.append(raw['legs']['steps']['start_location'])
        for path in raw['legs']['steps']:
            route.append(raw['legs']['steps']['end_location'])