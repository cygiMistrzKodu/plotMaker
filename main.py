from kivy.app import App
from kivy.core.window import Window

from interest_rate_input_view import InterestRateInput
# noinspection PyUnresolvedReferences
from interest_rate_result_view import InterestRateResultView  # used in .kv
from i18n.i18n import set_language

Window.minimum_width = 795
Window.minimum_height = 450
Window.size = (760, 450)


class PlotMakerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ = set_language('pl')
        # self._ = set_language('en')

    def build(self):
        return InterestRateInput()


if __name__ == "__main__":
    PlotMakerApp().run()
