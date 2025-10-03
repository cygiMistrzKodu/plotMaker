from typing import TypeAlias

from kivy.app import App
from kivy.properties import StringProperty

from interfaces.user_deposit import UserDeposit

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from decimal import getcontext

from interest_rate.calculator import InterestRateCalculator
from validation.user_deposit_validation import UserDepositValidator
from language_selector.language_selector import LanguageSelector  # for .kv

ERROR_FIELDS = {
    "depositAmountErrorKey": "depositAmountError",
    "depositTimeMonthsErrorKey": "depositTimeMonthsError",
    "bankInterestRateErrorKey": "bankInterestRateError",
}

getcontext().prec = 100

Builder.load_file("language_selector/language_selector.kv")
Builder.load_file("interest_rate_input.kv")

DepositErrors: TypeAlias = dict[str, str]


class InterestRateInput(BoxLayout):
    depositAmountError = StringProperty("")
    depositAmountErrorKey = StringProperty("")
    depositTimeMonthsError = StringProperty("")
    depositTimeMonthsErrorKey = StringProperty("")
    bankInterestRateError = StringProperty("")
    bankInterestRateErrorKey = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_deposit_validator = UserDepositValidator()

    def translate(self, key: str) -> str:
        return App.get_running_app()._(key)

    def validate_deposit_amount(self, text_input: TextInput):
        error_key = self.user_deposit_validator.validate_deposit_amount(text_input)
        if error_key:
            self.depositAmountErrorKey = error_key
        else:
            self.depositAmountErrorKey = ""
            self.depositAmountError = ""

    def validate_deposit_time(self, text_input: TextInput):
        error_key = self.user_deposit_validator.validate_deposit_time(text_input)
        if error_key:
            self.depositTimeMonthsErrorKey = error_key
        else:
            self.depositTimeMonthsErrorKey = ""
            self.depositTimeMonthsError = ""

    def validate_bank_interest_rate(self, text_input: TextInput):
        error_key = self.user_deposit_validator.validate_bank_interest_rate(text_input)
        if error_key:
            self.bankInterestRateErrorKey = error_key
        else:
            self.bankInterestRateErrorKey = ""
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

        for key_error_field, gui_error_label in ERROR_FIELDS.items():
            error_key = errors.get(key_error_field, "")
            setattr(self, key_error_field, error_key)
            setattr(self, gui_error_label, self.translate(error_key) if error_key else "")

    def _append_interest_rate_result(self, deposit_data):
        if self.ids.intrest_rate_result.data is None:
            self.ids.intrest_rate_result.data = []
        self.ids.intrest_rate_result.data.insert(0, self.calculate_interest(deposit_data))

    def refresh_texts(self):

        labels_translations = {
            "deposit_amount_label": self.translate("Deposit"),
            "deposit_time_label": self.translate("Deposit term"),
            "annual_interest_rate_label": self.translate("Bank interest"),
            "calculate_button": self.translate("Calculate"),
        }
        for widget_id, translated_text in labels_translations.items():
            if widget_id in self.ids:
                self.ids[widget_id].text = translated_text

        inputs_translations = {
            "deposit_input_id": self.translate("Deposit zł"),
            "deposit_time_input_id": self.translate("Time in months"),
            "bank_interest_rate_input_id": self.translate("Interest rate %"),
        }
        for widget_id, translated_text in inputs_translations.items():
            if widget_id in self.ids:
                self.ids[widget_id].hint_text = translated_text

        for key_error_field, gui_error_label in ERROR_FIELDS.items():
            error_key = getattr(self, key_error_field, "")
            setattr(self, gui_error_label, self.translate(error_key) if error_key else "")

        self._refresh_texts_in_children()

    def _refresh_texts_in_children(self):
        for child in self.walk():
            if child is not self and hasattr(child, "refresh_texts"):
                child.refresh_texts()
