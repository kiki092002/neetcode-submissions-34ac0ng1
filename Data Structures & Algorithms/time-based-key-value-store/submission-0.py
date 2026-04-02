class TimeMap:

    def __init__(self):
        self.hm = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        
        self.hm[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ''
        result = ''
        for v,t in self.hm[key]:
            if t<=timestamp:
                result = v
            else:
                break
        return result
