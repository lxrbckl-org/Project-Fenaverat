from json import loads

from src.view import View
from src.callbacks import Callbacks
from src.config import (app, port, fileLayout)


app.layout = View(loads(fileLayout)).build
Callbacks().register()
server = app.server


if (__name__ == "__main__"): app.run(

    port = port,
    debug = True

)