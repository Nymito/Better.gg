import requests
from dotenv import load_dotenv
import os

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

if not RIOT_API_KEY:
    print("❌ Clé API non trouvée dans le fichier .env")
    exit()

headers = {"X-Riot-Token": RIOT_API_KEY}
summoner_name = "Faker"  # Tu peux le changer
region = "euw1"

url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"

response = requests.get(url, headers=headers)

print("➡ URL:", url)
print("➡ Code HTTP:", response.status_code)
print("➡ Contenu:", response.json())