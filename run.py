from api import app
import sys


if __name__ == '__main__':
    args = sys.argv
    debug = True if '-debug' in args else False

    app.run(host='0.0.0.0', port=8000, debug=debug)
