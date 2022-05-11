import sys
import asyncio
from api import app


async def test(*args):
    print("test start", args)
    await asyncio.sleep(5)
    print("loop end")


if __name__ == '__main__':
    args = sys.argv
    debug = True if '-debug' in args else False

    app.run(host='0.0.0.0', port=8000, debug=debug)
