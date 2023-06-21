import pytest
from loguru import logger

from configuration import ACCESS_KEY, LOG_PATH
from currency_client.client import CurrencyClient


@pytest.fixture(scope="module", autouse=True)
def logging():
    logger.add(LOG_PATH / f"test_currency_client.log", format="{time} {level} {message}", level="DEBUG", mode='w')


@pytest.fixture(scope="session")
def currency_client():
    currency_client = CurrencyClient(access_key=ACCESS_KEY)
    currency_client.set_time_interval(minutes=1)
    return currency_client
