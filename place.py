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
    def __init__(self, address: str = None, name: str = None, rating: float = None, 
                    time: OpeningHours = None, price_rating: int = None, categories: list = []):
        self.address = address
        self.name = name
        self.rating = rating
        self.open_hours = time
        self.price_rating = price_rating
        self.categories = categories
        
        

    def from_raw(self, raw: dict) -> None:
        #self.address = raw[""]
