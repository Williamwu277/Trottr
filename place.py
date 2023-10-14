class OpeningHours:
     #{'open_now': False, 
     #'periods': [
     #   {'close': {'date': '2023-10-16', 'day': 1, 'time': '0000'}, 
     #   'open': {'date': '2023-10-15', 'day': 0, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-17', 'day': 2, 'time': '0000'}, 
     #   'open': {'date': '2023-10-16', 'day': 1, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-18', 'day': 3, 'time': '0000'}, 
     #   'open': {'date': '2023-10-17', 'day': 2, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-19', 'day': 4, 'time': '0000'}, 
     #   'open': {'date': '2023-10-18', 'day': 3, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-20', 'day': 5, 'time': '0000'}, 
     #   'open': {'date': '2023-10-19', 'day': 4, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-20', 'day': 5, 'time': '2359', 'truncated': True}, 
     #   'open': {'date': '2023-10-20', 'day': 5, 'time': '1030'}}, 
     #   {'close': {'date': '2023-10-15', 'day': 0, 'time': '0000'}, 
     #   'open': {'date': '2023-10-14', 'day': 6, 'time': '1030'}}], 
    #'weekday_text': ['Monday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Tuesday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Wednesday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Thursday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Friday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Saturday: 10:30\u202fAM\u2009–\u200912:00\u202fAM', 'Sunday: 10:30\u202fAM\u2009–\u200912:00\u202fAM']}
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
    def __init__(self, address: str = None, name: str = None, rating: float = None, time: OpeningHours = None, categories: list = []):
        self.address = address
        self.name = name
        self.rating = rating
        self.OpeningHours = OpeningHours
        self.categories = categories
        
        

    def from_raw(self, raw: dict) -> None:
        self.address = raw[""]

OpeningHours({'open_now': False, 
     'periods': [
        {'close': {'date': '2023-10-16', 'day': 1, 'time': '0000'}, 
        'open': {'date': '2023-10-15', 'day': 0, 'time': '1030'}}, 
        {'close': {'date': '2023-10-17', 'day': 2, 'time': '0000'}, 
        'open': {'date': '2023-10-16', 'day': 1, 'time': '1030'}}, 
        {'close': {'date': '2023-10-18', 'day': 3, 'time': '0000'}, 
        'open': {'date': '2023-10-17', 'day': 2, 'time': '1030'}}, 
        {'close': {'date': '2023-10-19', 'day': 4, 'time': '0000'}, 
        'open': {'date': '2023-10-18', 'day': 3, 'time': '1030'}}, 
        {'close': {'date': '2023-10-20', 'day': 5, 'time': '0000'}, 
        'open': {'date': '2023-10-19', 'day': 4, 'time': '1030'}}, 
        {'close': {'date': '2023-10-20', 'day': 5, 'time': '2359', 'truncated': True}, 
        'open': {'date': '2023-10-20', 'day': 5, 'time': '1030'}}, 
        {'close': {'date': '2023-10-15', 'day': 0, 'time': '0000'}, 
        'open': {'date': '2023-10-14', 'day': 6, 'time': '1030'}}]} )