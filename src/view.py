from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class View:


    def __init__(self, items):
        """  """

        self.items = items


    def _buildItem(
            
            self,
            row = 1, 
            col = 1,
            text = [],
            style = {},
            visible = True,
            background = None

        ):
        """  """

        return html.Div(

            className = "gridItem",
            children = dcc.Markdown(

                children = "\n".join(text),
                className = "markdownExtended"

            ),
            style = {

                **style,
                "grid-row" : f"span {row}",
                "grid-column" : f"span {col}",
                "background-image" : f"url({background})",
                "visibility" : "visible" if visible else "hidden"

            }

        )


    @property
    def build(self):
        """  """

        return dmc.MantineProvider(children = dmc.Center(children = [

            html.Div(

                className = "gridContainer",
                children = [self._buildItem(**i) for i in self.items]

            )

        ]))