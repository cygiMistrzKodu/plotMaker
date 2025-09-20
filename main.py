from kivy.app import App
from kivy.clock import Clock
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
        self.original_size = None
        # self._ = set_language('pl')
        self._ = set_language('en')

    def build(self):
        self.original_size = Window.size
        Clock.schedule_once(self.refresh_window_layout, 0.1)
        return InterestRateInput()

    def refresh_window_layout(self, dt):
        Window.size = (self.original_size[0] + 1, self.original_size[1] + 1)

        Clock.schedule_once(self.restore_window_size, 0.1)

    def restore_window_size(self, dt):
        Window.size = self.original_size


if __name__ == "__main__":
    PlotMakerApp().run()
