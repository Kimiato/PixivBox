from sanic.response import json

from api.core import Pixiv
from api.core.utils import i_img_url_replace

async def get_recommend(request):
    """插画推荐
    :param request:
    offset: [可选] 偏移
    """
    offset = request.args.get('offset')
    result = await Pixiv().api.illust_recommended(offset=offset)
    i_img_url_replace(result)
    return json(result)
