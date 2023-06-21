import requests
from datetime import timedelta
from currency_client.cache import Cache
from configuration import SERVICE_URL
from loguru import logger


class CurrencyClient:
    def __init__(self, access_key):
        self.access_key = access_key
        self.cache = Cache()

    def get_currency(self, left_currency_code: str, right_currency_code: str):
        cached_value = self.cache.get(left_currency_code)

        if cached_value:
            logger.info(f'Get cached data of {left_currency_code} - {cached_value}')
            return cached_value

        url = f'{SERVICE_URL}/latest?base={left_currency_code}'
        headers = {
            "apikey": self.access_key
        }

        logger.info(f'{url} - GET')

        response = requests.get(url=url, headers=headers)
        logger.info(f"{url} - {response.status_code} - {response.json()['rates'][right_currency_code]}")
        response.raise_for_status()

        rate = response.json()['rates'][right_currency_code]
        logger.success(rate)
        self.cache.set(left_currency_code, rate)

        return rate

    def set_time_interval(self, minutes: int = 0, seconds: int = 0):
        self.cache.duration = timedelta(minutes=minutes, seconds=seconds)
        logger.debug(f"New expire interval {self.cache.duration=}")

    def clear_cache(self):
        self.cache.clear()
