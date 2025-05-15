from kivy.app import App
from kivy.uix.label import Label


class PlotMakerApp(App):
    def build(self):
        return Label(text="Wtaj w Kivy plot!")


if __name__ == "__main__":
    PlotMakerApp().run()
