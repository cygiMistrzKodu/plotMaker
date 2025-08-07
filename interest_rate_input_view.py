from interfaces.user_deposit import UserDeposit

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from decimal import getcontext

from interest_rate.calculator import InterestRateCalculator

getcontext().prec = 100

Builder.load_file("interest_rate_input.kv")

class InterestRateInput(BoxLayout):

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
        data: UserDeposit = {
            "depositAmount": self.ids.deposit_input_id.text,
            "depositTimeMonths": self.ids.deposit_time_input_id.text,
            "bankInterestRate": self.ids.bank_interest_rate_input_id.text
        }
        return data

    def get_deposit_data(self) -> UserDeposit:
        return self.get_user_input()

    def calculate_interest(self, deposit_data: UserDeposit) -> dict:

        interest_rate_calculator = InterestRateCalculator(deposit_data["depositAmount"]
                                                          , deposit_data["depositTimeMonths"],
                                                          deposit_data["bankInterestRate"])

        return interest_rate_calculator.calculate()

    def calculate_interest_rate(self):

        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []

        self.ids.intrest_rate_result.data.insert(0, self.calculate_interest(self.get_deposit_data()))
