from sanic.response import json

from api.core import Pixiv
from api.core.utils import i_img_url_replace

async def get_recommend(request):
    """插画推荐
    """
    result = await Pixiv().api.illust_recommended()
    i_img_url_replace(result)
    return json(result)
