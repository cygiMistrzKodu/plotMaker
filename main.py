from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


Builder.load_file("intrest_rate_input.kv")


class IntrestRateInput(BoxLayout):

    def process_intrest(self, text_input: TextInput):
        self.validate_in_percent_range(text_input)

    def validate_in_percent_range(self, text_input: TextInput):
        try:
            interest = float(text_input.text.strip("%"))

            if interest > 100 or interest < 0:
                text_input.foreground_color = (1, 0, 0, 1)
            else:
                text_input.foreground_color = (0, 0, 0, 1)

        except ValueError:
            text_input.foreground_color = (1, 0, 0, 1)


if __name__ == "__main__":
    PlotMakerApp().run()
