import os
import aiofiles


async def load_file(file_path):
    if not os.path.exists(file_path):
        return None
    async with aiofiles.open(file_path, mode='rb') as f:
        return await f.read()


async def write_file(file_path, data):
    async with aiofiles.open(file_path, mode='wb') as f:
        await f.write(data)