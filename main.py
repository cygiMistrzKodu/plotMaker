from typing import TypedDict

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# noinspection PyUnresolvedReferences
from intrest_rate_result_view import IntrestRateResultView  # used in .kv

from kivy.core.window import Window

Window.minimum_width = 795
Window.minimum_height = 450
Window.size = (760, 450)

class PlotMakerApp(App):
    def build(self):
        return IntrestRateInput()


class DepositType(TypedDict):
    depositAmount: str
    depositTime: str
    annualInterestRate: str


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

    def get_user_input(self):
        data: DepositType = {
            "depositAmount": self.ids.deposit_input_id.text,
            "depositTime": self.ids.deposit_time_input_id.text,
            "annualInterestRate": self.ids.annual_interest_rate_input_id.text
        }
        return data

    def add_some_data_test(self):
        deposit_input: DepositType = self.get_user_input()

        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []

            # ToDO dostosować wyjście do moich preferencji czyli najpierw dla jakich danych obliczenia a potem odsetkii z tego

        self.ids.intrest_rate_result.data.insert(0, deposit_input)

        print("Dodano dane do RecycleView!")


if __name__ == "__main__":
    PlotMakerApp().run()
