from sanic import Sanic

from .core.pixiv import refresh_token

app = Sanic('pixiv-box')
app.static('/', './static')
app.static('/', './static/index.html')
app.add_task(refresh_token)