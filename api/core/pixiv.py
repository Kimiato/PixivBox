import asyncio
from pixivpy_async.sync import PixivClient, AppPixivAPI

from .utils import load_file, write_file
from .auth_helper import login, refresh

class Pixiv:
    def __init__(self):
        self.client = PixivClient(proxy="socks5://127.0.0.1:10808")
        # self.client = PixivClient()
        self.api = AppPixivAPI(client=self.client)

    async def _login(self, *args):
        self.refresh_token = await load_file('.refresh_token')
        if self.refresh_token is None:
            self.refresh_token = login()["refresh_token"]
            await self._write_token()
        # else:
            # self.access_token = await refresh(self.refresh_token)['refresh_token']
        result = await self.api.login(refresh_token=self.refresh_token)
        self.access_token = result.access_token
        await asyncio.sleep(60 * 60)

    async def _write_token(self):
        await write_file('.refresh_token', self.access_token)

pixiv = Pixiv()
