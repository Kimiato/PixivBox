from sanic.response import json

from api.core import pixiv

async def get_recommend(request):
    json_result = await pixiv.api.illust_recommended()
    return json(json_result)
