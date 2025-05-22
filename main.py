from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


Builder.load_file("intrest_rate_input.kv")


class IntrestRateInput(BoxLayout):
    pass


if __name__ == "__main__":
    PlotMakerApp().run()
