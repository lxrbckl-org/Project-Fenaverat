from src.services import Services
from dash.dependencies import (Input, Output, State, ALL)


class Callbacks:


    def __init__(self, services):
        """  """

        self.services = services
    

    def register(self):
        """  """

        pass


    def nIntervalsCallback(self):
        """  """

        @app.callback(



        )
        def func(*args): self.services.nIntervalService(*args)