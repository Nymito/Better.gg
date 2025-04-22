from fastapi import APIRouter
from app.services.riot_api import get_summoner_data

router = APIRouter()

@router.api_route("/summoner/{summoner_name}")
def summoner_info(summoner_name: str):
    return get_summoner_data(summoner_name)