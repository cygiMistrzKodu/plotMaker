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

        # przemyślnie  Wynik z odsetkami i ile w sumie będzie miał to jedno pole.
        # a te 3 jak sobie podzieliłem dzienne, miesięczne i roczne do licze jak dla jednego miesiaca
        # wynik ile odsetek do 2 pola: jedno ile dostaniesz odsetek. a drugie ile dostanie odestek odejmując podatek belki
        # może być też pole jaka jest cała kwota całośćiowa i drugie pole odejmujące podatek belki

        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []

        intrest_rate_result.update(
            {"dailyIntrestRateIncrease": f"{daly_intrest_rate_increase:.3f}",
             "monthlyIntrestRateIncrease": f"{monthly_intrest_rate_increase:.3f}",
             "annualIntrestRateIncrease": f"{annual_intrest_rate_increase:.3f}"})

        self.ids.intrest_rate_result.data.insert(0, intrest_rate_result)

        print(self.ids.keys())

        print("Dodano dane do RecycleView!")
