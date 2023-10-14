class OpeningHours:
    def __init__(self, raw : dict):
        pass

class Place:
    def __init__(self, address: str = None, name: str = None, rating: float = None, time: OpeningHours = None, categories: list = []):
        self.address = address
        
        

    def from_raw(self, raw: dict) -> None:
        pass