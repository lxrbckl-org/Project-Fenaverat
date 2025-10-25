from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class View:


    def __init__(self):
        """  """

        pass


    def _buildItem(
            
            row = 1, 
            col = 1,
            style = {},
            text = None,
            visible = True,
            background = None

        ):
        """  """

        return html.Div(

            className = "gridItem",
            children = dcc.Markdown(

                children = text,
                className = "markdownCustom"

            ),
            style = {

                **style,
                "grid-row" : f"span {row}",
                "grid-col" : f"span {col}",
                "visibility" : "visible" if visible else "hidden",
                **{}
                # todo insert data
                # todo insert background

            }

        )


    @property
    def build(self, items):
        """  """

        return dmc.MantineProvider(children = dmc.Center(children = [

            html.Div(

                className = "gridContainer",
                children = [View._buildItem(i) for i in items]

            )

        ]))