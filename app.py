from src.view import View
from src.config import (app, port)
from src.callbacks import Callbacks


app.layout = View().build
Callbacks().register()
server = app.server


if (__name__ == "__main__"): app.run(

    port = port,
    debug = True

)