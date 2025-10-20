from os import getenv
from dash import Dash
from pathlib import Path
from dash_bootstrap_components import themes


port = getenv("PORT", 8056)
host = getenv("HOST", "0.0.0.0")

root = Path(__file__).resolve().parent.parent
dirData = root / "data"
dirAssets = root / "src" / "assets"


app = Dash(

    name = "Project Fenaverat",
    title = "Project Fenaverat",
    assets_folder = "src/assets",
    suppress_callback_exceptions = True,
    external_stylesheets = [

        # themes.GRID,
        themes.BOOTSTRAP

    ]

)