from sanic.response import json

from api.core import aapi

async def get_recommend(request):
    json_result = await aapi.illust_recommended()
    return json(json_result)
