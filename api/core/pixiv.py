from pixivpy_async.sync import PixivClient, AppPixivAPI

client = PixivClient()
aapi = AppPixivAPI(client=client.start())
