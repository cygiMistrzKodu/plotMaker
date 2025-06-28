from kivy.app import App
from kivy.core.window import Window

from intrest_rate_input_view import IntrestRateInput
# noinspection PyUnresolvedReferences
from intrest_rate_result_view import IntrestRateResultView  # used in .kv

Window.minimum_width = 795
Window.minimum_height = 450
Window.size = (760, 450)


class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


if __name__ == "__main__":
    PlotMakerApp().run()
