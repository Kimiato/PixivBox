from sanic.response import json
from sanic.exceptions import BadURL

from api.core import Pixiv
from api.core.utils import i_img_url_replace


def validate_mode(value):
    if value not in ['day', 'week', 'month', 'day_male', 'day_female',
        'week_original', 'week_rookie', 'day_manga']:
        raise BadURL


async def get_rank(request):
    """获取排名
    :request param:
    mode: [必选] day, week, month, day_male, day_female, week_original, week_rookie, day_manga
    offset: [可选] 偏移多少页
    date: [可选] string
    """
    mode = request.args.get("mode")
    validate_mode(mode)
    offset = request.args.get('offset')
    date = request.args.get('date')

    result = await Pixiv().api.illust_ranking(mode=mode, offset=offset, date=date)
    i_img_url_replace(result)
    return json(result)
