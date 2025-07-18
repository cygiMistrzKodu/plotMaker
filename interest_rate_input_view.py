from numbers import Number
from typing import TypedDict, NotRequired

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from decimal import Decimal, getcontext

getcontext().prec = 100


class DepositType(TypedDict):
    depositAmount: str
    depositTimeMonths: str
    bankInterestRate: str
    annualIntrestRateIncrease: NotRequired[str]
    monthlyIntrestRateIncrease: NotRequired[str]
    dailyIntrestRateIncrease: NotRequired[str]
    intrestRateNet: NotRequired[str]
    intrestRateGross: NotRequired[str]


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
        data: DepositType = {
            "depositAmount": self.ids.deposit_input_id.text,
            "depositTimeMonths": self.ids.deposit_time_input_id.text,
            "bankInterestRate": self.ids.bank_interest_rate_input_id.text
        }
        return data

    def add_some_data_test(self):

        intrest_rate_result: DepositType = self.get_user_input()

        deposit_amount = intrest_rate_result["depositAmount"]
        deposit_time_months = intrest_rate_result["depositTimeMonths"]
        bank_interest_rate = intrest_rate_result["bankInterestRate"]

        annual_intrest_rate_increase = (Decimal(deposit_amount) * (Decimal(bank_interest_rate) / 100))

        monthly_intrest_rate_increase = (Decimal(deposit_amount)
                                         * ((Decimal(bank_interest_rate) / 100) / 12))

        daly_intrest_rate_increase = Decimal(deposit_amount) * (Decimal(bank_interest_rate) / 100 / 365)

        intrest_rate_gross = ((Decimal(deposit_amount) * (Decimal(bank_interest_rate) / 100))
                              * (Decimal(deposit_time_months)) / 12)

        intrest_rate_net = intrest_rate_gross * Decimal(0.81)

        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []

        intrest_rate_result.update(
            {"dailyIntrestRateIncrease": f"{daly_intrest_rate_increase:.3f}",
             "monthlyIntrestRateIncrease": f"{monthly_intrest_rate_increase:.3f}",
             "annualIntrestRateIncrease": f"{annual_intrest_rate_increase:.3f}",
             "intrestRateGross": f"{intrest_rate_gross:.3f}",
             "intrestRateNet": f"{intrest_rate_net:.3f}",
             })

        self.ids.intrest_rate_result.data.insert(0, intrest_rate_result)

        print(self.ids.keys())

        print("Dodano dane do RecycleView!")
