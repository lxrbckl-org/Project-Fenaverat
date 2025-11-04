from dash.html import (Div, Video)
import dash_mantine_components as dmc
from dash.dcc import (Markdown, Interval)


class View:


    def __init__(self, items):
        """  """

        self.items = items


    def _buildItem(
            
            self,
            row = 1, 
            col = 1,
            style = {},
            corpus = [],
            video = None,
            visible = True,
            background = None,
            align = "center-top"

        ):
        """  """

        return Div(

            className = "gridItem",
            children = Video(

                src = video,
                loop = False,
                muted = True,
                autoPlay = False,
                className = "videoExtended",
                id = {"type" : "video", "index" : video}

            ) if video else Markdown(

                className = "markdownExtended",
                children = "\n".join([
                    
                    {

                        str: c,
                        list: " ".join(f"`{b}`" for b in c) + "\n"

                    }[type(c)]

                for c in corpus])

            ),
            style = {

                **style,
                "alignItems" : align,
                "gridRow" : f"span {row}",
                "gridColumn" : f"span {col}",
                "backgroundImage" : f"url({background})",
                "visibility" : "visible" if visible else "hidden"

            }

        )


    @property
    def build(self):
        """  """

        return dmc.MantineProvider(children = dmc.Center(children = [

            Interval(

                n_intervals = 0,
                id = "intervalId",
                interval = (1000 * 60)

            ),
            Div(

                className = "gridContainer",
                children = [self._buildItem(**i) for i in self.items]

            )

        ]))