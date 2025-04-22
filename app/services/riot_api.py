import os
import requests
from dotenv import load_dotenv

from app.utils.typed_dict import SummonerInfo


load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
BASE_URL = "https://euw1.api.riotgames.com"

def get_summoner_data(summoner_name: str) -> SummonerInfo:
    url = f"{BASE_URL}/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()