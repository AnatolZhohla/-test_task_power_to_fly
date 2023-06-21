import time
from loguru import logger


def test_get_currency_returns_rate(currency_client):
    logger.info('Starting test: test_get_currency_returns_rate')
    currency_code = 'USD'
    rate = currency_client.get_currency(currency_code, 'EUR')
    assert isinstance(rate, float)


def test_get_currency_caches_data(currency_client):
    logger.info('Starting test: test_get_currency_caches_data')
    currency_code = 'USD'
    rate1 = currency_client.get_currency(currency_code, 'EUR')
    rate2 = currency_client.get_currency(currency_code, 'EUR')
    assert rate1 == rate2


def test_cache_expiration(currency_client):
    logger.info('Starting test: test_cache_expiration')
    currency_code = 'USD'
    rate1 = currency_client.get_currency(currency_code, 'EUR')
    time.sleep(65)  # Wait for cache duration to expire (65 seconds to be safe)
    rate2 = currency_client.get_currency(currency_code, 'EUR')
    assert rate1 != rate2
    assert rate2 is not None
