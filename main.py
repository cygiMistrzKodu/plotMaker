from kivy.app import App
from kivy.core.window import Window

from interest_rate_input_view import InterestRateInput
# noinspection PyUnresolvedReferences
from interest_rate_result_view import InterestRateResultView  # used in .kv

Window.minimum_width = 795
Window.minimum_height = 450
Window.size = (760, 450)


class PlotMakerApp(App):
    def build(self):
        return InterestRateInput()


if __name__ == "__main__":
    PlotMakerApp().run()
