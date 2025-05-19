from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


Builder.load_file("intrest_rate_input.kv")


class IntrestRateInput(BoxLayout):
    pass


if __name__ == "__main__":
    PlotMakerApp().run()
