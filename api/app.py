from sanic import Sanic

from .core.pixiv import refresh_token
from sanic_cors import CORS

app = Sanic('pixiv-box')
CORS(app)
app.static('/', './static')
app.static('/', './static/index.html')
app.add_task(refresh_token)
