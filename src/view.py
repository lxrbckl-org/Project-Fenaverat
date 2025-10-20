from dash import (html, dcc)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


class View:


    def __init__(self):
        """  """

        pass


    def _buildItem(row, col, visible, style):
        """  """

        return html.Div(

            

        )


    @staticmethod
    def buildItemText(children):
        """  """
    
        return dcc.Markdown(

            children = children,
            className = "markdownExtended"

        )


    @staticmethod
    def buildItemImage(src):
        """  """

        return dmc.Image(

            src = src,
            className = "imageExtended"

        )


    @property
    def build(self):
        """  """

        return dmc.MantineProvider(children = dmc.Center(

            className = "centerExtended",
            children = [

                html.Div(

                    className = "gridContainer",
                    children = [

                        html.Div(children="", className="gridItemVisible sample4"),
                        html.Div(children="", className="gridItemVisible sample1"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible"),
                        html.Div(children="", className="gridItemVisible"),
                        html.Div(children="", className="gridItemVisible sample3"),
                        html.Div(children="", className="gridItemVisible sample3 gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible sample2"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible"),
                        html.Div(children="", className="gridItemVisible sample2"),
                        html.Div(children="", className="gridItemVisible"),
                        html.Div(children="", className="gridItemVisible sample5"),
                        html.Div(children="", className="gridItemVisible"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible sample5"),
                        html.Div(children="", className="gridItemVisible sample5 gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible sample 2"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible"),
                        html.Div(children="", className="gridItemVisible sample 2"),
                        html.Div(children="", className="gridItemVisible gridItemInvisible")

                    ]

                )

            ]

        ))
















# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Full-Width Responsive Grid</title>

# </head>
# <body>

# <div class="grid-container">
#   <div class="item1">1</div>
#   <div class="item2">2</div>
#   <div class="item3">3</div>
#   <div class="item4">4</div>
#   <div class="item5">5</div>
#   <div class="item6">6</div>
#   <div class="item7">7</div>
#   <div class="item8">8</div>
#   <div class="item9">9</div>
#   <div class="item10">10</div>
#   <div class="item11">11</div>
#   <div class="item12">12</div>
#   <div class="item13">13</div>
#   <div class="item14">14</div>
#   <div class="item15">15</div>
#   <div class="item1">1</div>
#   <div class="item2">2</div>
#   <div class="item3">3</div>
#   <div class="item4">4</div>
#   <div class="item5">5</div>
#   <div class="item6">6</div>
#   <div class="item7">7</div>
#   <div class="item8">8</div>
#   <div class="item9">9</div>
#   <div class="item10">10</div>
#   <div class="item11">11</div>
#   <div class="item12">12</div>
#   <div class="item13">13</div>
#   <div class="item14">14</div>
#   <div class="item15">15</div>
# </div>

# </body>
# </html>