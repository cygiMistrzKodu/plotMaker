from typing import TypeAlias

from kivy.properties import StringProperty

from interfaces.user_deposit import UserDeposit

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from decimal import getcontext

from interest_rate.calculator import InterestRateCalculator
from validation.user_deposit_validation import UserDepositValidator

getcontext().prec = 100

Builder.load_file("interest_rate_input.kv")

DepositErrors: TypeAlias = dict[str, str]


class InterestRateInput(BoxLayout):
    depositAmountError = StringProperty("")
    depositTimeMonthsError = StringProperty("")
    bankInterestRateError = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_deposit_validator = UserDepositValidator()

    def validate_deposit_amount(self, text_input: TextInput):
        error = self.user_deposit_validator.validate_deposit_amount(text_input)
        if error:
            self.depositAmountError = error
        else:
            self.depositAmountError = ""

    def validate_deposit_time(self, text_input: TextInput):
        error = self.user_deposit_validator.validate_deposit_time(text_input)
        if error:
            self.depositTimeMonthsError = error
        else:
            self.depositTimeMonthsError = ""

    def validate_bank_interest_rate(self, text_input: TextInput):
        error = self.user_deposit_validator.validate_bank_interest_rate(text_input)
        if error:
            self.bankInterestRateError = error
        else:
            self.bankInterestRateError = ""

    def get_user_input(self) -> UserDeposit:
        data: UserDeposit = {
            "depositAmount": self.ids.deposit_input_id.text,
            "depositTimeMonths": self.ids.deposit_time_input_id.text,
            "bankInterestRate": self.ids.bank_interest_rate_input_id.text
        }
        return data

    def get_deposit_data(self) -> tuple[UserDeposit | None, DepositErrors]:
        user_deposit_input = self.get_user_input()
        errors = self.user_deposit_validator.validate_deposit_form(user_deposit_input)
        return (None, errors) if errors else (user_deposit_input, {})

    def calculate_interest(self, deposit_data: UserDeposit) -> dict:

        interest_rate_calculator = InterestRateCalculator(deposit_data["depositAmount"]
                                                          , deposit_data["depositTimeMonths"],
                                                          deposit_data["bankInterestRate"])

        return interest_rate_calculator.calculate()

    def calculate_interest_rate(self):

        deposit_data, errors = self.get_deposit_data()

        self._update_error_labels(errors)

        if errors:
            return

        self._append_interest_rate_result(deposit_data)

    def _update_error_labels(self, errors):
        for field in ["depositAmountError", "depositTimeMonthsError", "bankInterestRateError"]:
            setattr(self, field, errors.get(field, ""))

    def _append_interest_rate_result(self, deposit_data):
        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []
        self.ids.intrest_rate_result.data.insert(0, self.calculate_interest(deposit_data))
