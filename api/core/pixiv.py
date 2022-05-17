import asyncio
from pixivpy_async.sync import PixivClient, AppPixivAPI
from sanic.log import logger

from api import config

from .utils import load_file, write_file, Singleton
from .auth_helper import login, refresh


@Singleton
class Pixiv:
    def __init__(self):
        self.proxy = getattr(config, 'PROXY', None)
        self.client = PixivClient(proxy=self.proxy)
        self.api = AppPixivAPI(client=self.client)

    async def _login(self, *args):
        self.refresh_token = await load_file('.refresh_token')
        if self.refresh_token is None:
            rst = await login()
            self.refresh_token = rst["refresh_token"]
        else:
            rst = await refresh(self.refresh_token)
            self.refresh_token = rst['refresh_token']
        await self._write_token()
        await self.api.login(refresh_token=self.refresh_token)
        logger.info("refresh token and login success")

    async def _write_token(self):
        await write_file('.refresh_token', self.refresh_token)

async def refresh_token(*args):
    while True:
        await Pixiv()._login(*args)
        await asyncio.sleep(60 * 60)
