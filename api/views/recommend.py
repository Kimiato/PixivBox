from sanic.response import json

from api.core import Pixiv

async def get_recommend(request):
    json_result = await Pixiv().api.illust_recommended()
    return json(json_result)
