from sanic.exceptions import InvalidUsage
from sanic.response import json

from api.core import Pixiv
from api.core.utils import i_img_url_replace


def validateData(request):
    if not request.args.get("word"):
        raise InvalidUsage("word is required")
    if request.args.get('duration') and request.args.get('duration') not in [
        'within_last_day', 'within_last_week', 'within_last_month']:
        raise InvalidUsage("duration is invalid")


async def search(request):
    """搜索
    :request param:
    word: [必选] 搜索关键字
    douration: [可选] 搜索时间范围 [within_last_day, within_last_week, within_last_month]
    start_date: [可选] string
    end_date: [可选] string
    """
    validateData(request)
    word = request.args.get("word")
    duration = request.args.get("duration")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    result = await Pixiv().api.search_illust(word=word,
        duration=duration, start_date=start_date, end_date=end_date)
    i_img_url_replace(result)

    return json(result)
