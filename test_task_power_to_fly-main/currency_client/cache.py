from datetime import datetime, timedelta


class Cache:
    def __init__(self, duration: timedelta = timedelta(seconds=0)):
        self.duration = duration
        self.data = {}

    def get(self, currency):
        if currency in self.data and datetime.utcnow() - self.data[currency]['timestamp'] < self.duration:
            return self.data[currency]['value']
        else:
            return None

    def set(self, key, value):
        self.data[key] = {'value': value, 'timestamp': datetime.utcnow()}

    def clear(self):
        self.data.clear()
