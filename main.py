from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


class IntrestRateInput(BoxLayout):
    def __init__(self):
        super().__init__(orientation="horizontal")

        self.capital_amount_label: Label = Label()
        self.capital_amount_label.text = "Kapitał"
        self.capital_amount_label.size = (10,20)

        self.capital_input: TextInput = TextInput(hint_text="Wpisz kapitał: ")
        self.add_widget(self.capital_amount_label)
        self.add_widget(self.capital_input)


if __name__ == "__main__":
    PlotMakerApp().run()
