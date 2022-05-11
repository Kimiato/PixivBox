from . import app
from api.views import get_recommend,get_rank


def add_base_route(handler, uri, methods=['GET', 'OPTIONS'], **ctx_kwargs):
    uri = "/api/" + uri
    if 'OPTIONS' not in methods:
        methods.append('OPTIONS')
    app.add_route(handler=handler, uri=uri, methods=methods, **ctx_kwargs)

add_base_route(get_recommend, 'recommend')
add_base_route(get_rank, 'rank')
