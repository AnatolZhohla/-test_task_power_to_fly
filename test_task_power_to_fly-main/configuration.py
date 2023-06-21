from pathlib import Path

SERVICE_URL = 'https://api.apilayer.com/exchangerates_data'
ACCESS_KEY = "ETUmPOSOCAOQUFKfQ08XV3pJZ2e2BFlH"

LOG_PATH = Path(__file__).resolve().parent / "logs"
LOG_PATH.mkdir(exist_ok=True)

