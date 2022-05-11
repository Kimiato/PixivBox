from sanic import Sanic

from .core.pixiv import refresh_token

app = Sanic('pixiv-box')
app.add_task(refresh_token)