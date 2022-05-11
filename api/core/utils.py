import os
import aiofiles

from api import config


async def load_file(file_path):
    if not os.path.exists(file_path):
        return None
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        return await f.read()


async def write_file(file_path, data):
    async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
        await f.write(data)


def Singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instance = cls(*args, **kwargs)
            instances[cls] = instance
        return instances[cls]
    return getinstance


def i_img_url_replace(result_dict: dict):
    """替换结果字典中的string"""

    def expland_dict_and_replace(source, replace_target, replace_value):
        """展开字典并替换str"""
        if isinstance(source, list):
            for i, v in enumerate(source):
                if isinstance(v, dict):
                    expland_dict_and_replace(v, replace_target, replace_value)
                elif isinstance(v, str):
                    source[i] = v.replace(replace_target, replace_value)
                elif isinstance(v, list):
                    expland_dict_and_replace(v, replace_target, replace_value)
            return

        for k, v in source.items():
            if isinstance(v, dict):
                expland_dict_and_replace(v, replace_target, replace_value)

            elif isinstance(v, list):
                for index, i in enumerate(v):
                    if isinstance(i, dict):
                        expland_dict_and_replace(i, replace_target, replace_value)
                    elif isinstance(i, str):
                        v[index] = i.replace(replace_target, replace_value)

            elif isinstance(v, str):
                source[k] = v.replace(replace_target, replace_value)

    replace_value = getattr(config, 'i_PXIMG_URL_REPLACE_VALUE')
    replace_target = 'https://i.pximg.net'
    if not replace_value:
        return
    for key, value in result_dict.items():
        if not isinstance(value, (str, int, float)):
            expland_dict_and_replace(value, replace_target, replace_value)
        elif isinstance(value, str):
            result_dict[key] = value.replace(replace_target, replace_value)
