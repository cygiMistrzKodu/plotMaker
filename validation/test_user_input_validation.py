from decimal import Decimal, InvalidOperation
from interfaces.user_deposit import UserDeposit

import pytest


class UserDepositValidator:
    EMPTY_FILED_MESSAGE = "field cannot be empty"
    CANNOT_HAVE_LETTERS_MESSAGE = "filed cannot have letters"
    CANNOT_BE_ZERO_OR_BELOW_MESSAGE = "filed cannot be less of equal to zero"
    CANNOT_BE_BIGGER_THAN_100_PERCENT = "filed cannot be bigger than 100%"

    def _validate_decimal(self, value) -> str | None:
        try:
            Decimal(value)
        except InvalidOperation:
            return self.CANNOT_HAVE_LETTERS_MESSAGE

    def _validate_decimal_above_zero(self, value) -> str | None:
        if Decimal(value) <= Decimal("0"):
            return self.CANNOT_BE_ZERO_OR_BELOW_MESSAGE
        return None

    def _validate_filed_not_empty(self, value) -> str | None:
        if value == "":
            return self.EMPTY_FILED_MESSAGE
        return None

    def validate_deposit_amount(self,
                                amount: str):

        error = self._validate_filed_not_empty(amount)
        if error:
            return error

        error = self._validate_decimal(amount)
        if error:
            return error

        error = self._validate_decimal_above_zero(amount)
        if error:
            return error

        return None

    def validate_deposit_time(self, time: str):

        if time == "":
            return self.EMPTY_FILED_MESSAGE

        error = self._validate_decimal(time)
        if error:
            return error

        error = self._validate_decimal_above_zero(time)
        if error:
            return error

        return None

    def validate_bank_interest_rate(self, bank_interest_rate):

        if bank_interest_rate == "":
            return self.EMPTY_FILED_MESSAGE

        error = self._validate_decimal(bank_interest_rate)
        if error:
            return error

        error = self._validate_decimal_above_zero(bank_interest_rate)
        if error:
            return error

        if Decimal(bank_interest_rate) > Decimal(100):
            return self.CANNOT_BE_BIGGER_THAN_100_PERCENT

        return None

    def validate_deposit_form(self, deposit: UserDeposit):

        errors: dict[str, str] = {"depositAmountError": self.validate_deposit_amount(deposit["depositAmount"]),
                                  "depositTimeMonthsError": self.validate_deposit_time(deposit["depositTimeMonths"]),
                                  "bankInterestRateError": self.validate_bank_interest_rate(
                                      deposit["bankInterestRate"])}

        errors = self._remove_keys_with_none(errors)

        return errors if errors else None

    def _remove_keys_with_none(self, errors):
        errors = {key: value for key, value in errors.items() if
                  value is not None}
        return errors


@pytest.fixture
def user_deposit_validator():
    return UserDepositValidator()


EMPTY_FILED_MESSAGE = "field cannot be empty"
CANNOT_HAVE_LETTERS_MESSAGE = "filed cannot have letters"
CANNOT_BE_ZERO_OR_BELOW_MESSAGE = "filed cannot be less of equal to zero"
CANNOT_BE_BIGGER_THAN_100_PERCENT = "filed cannot be bigger than 100%"


def test_deposit_amount_cannot_be_empty(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_amount("")
    assert message == EMPTY_FILED_MESSAGE


def test_deposit_amount_not_empty_is_ok(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_amount("6")
    assert message is None


def test_deposit_amount_cannot_have_letters(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_amount("llll8P")
    assert message == CANNOT_HAVE_LETTERS_MESSAGE


def test_deposit_amount_cannot_be_less_than_or_equal_to_zero(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_amount("-7")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_deposit_amount_cannot_be_equal_to_zero(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_amount("0")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_deposit_time_empty_validation(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_time("")
    assert message == EMPTY_FILED_MESSAGE


def test_deposit_time_ok_case(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_time("7")
    assert message is None


def test_deposit_time_cannot_be_0(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_time("0")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_deposit_time_cannot_be_less_than_0(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_time("-8")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_deposit_time_cannot_have_letters(user_deposit_validator):
    message = user_deposit_validator.validate_deposit_time("kk")
    assert message == CANNOT_HAVE_LETTERS_MESSAGE


def test_bank_interest_rate_empty_validation(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("")
    assert message == EMPTY_FILED_MESSAGE


def test_bank_interest_rate_not_empty_is_ok(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("8")
    assert message is None


def test_bank_interest_rate_cannot_have_letters(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("letters")
    assert message == CANNOT_HAVE_LETTERS_MESSAGE


def test_bank_interest_rate_cannot_be_0(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("0")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_bank_interest_rate_cannot_be_less_than_zero(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("-5")
    assert message == CANNOT_BE_ZERO_OR_BELOW_MESSAGE


def test_bank_interest_rate_cannot_be_bigger_than_100(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("101")
    assert message == CANNOT_BE_BIGGER_THAN_100_PERCENT

def test_bank_interest_rate_100_is_ok(user_deposit_validator):
    message = user_deposit_validator.validate_bank_interest_rate("100")
    assert message is None


def test_user_deposit_input_form_validation_all_fields_empty_return_three_keys_with_empty_errors_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "",
        "depositTimeMonths": "",
        "bankInterestRate": ""
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositAmountError": EMPTY_FILED_MESSAGE,
                      "depositTimeMonthsError": EMPTY_FILED_MESSAGE,
                      "bankInterestRateError": EMPTY_FILED_MESSAGE}


def test_user_deposit_input_form_validation_happy_path(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "14444",
        "depositTimeMonths": "6",
        "bankInterestRate": "3"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors is None


def test_user_deposit_input_form_validation_deposit_amount_empty_return_deposit_amount_error_key_with_error_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "",
        "depositTimeMonths": "3",
        "bankInterestRate": "3"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositAmountError": EMPTY_FILED_MESSAGE}


def test_user_deposit_input_form_validation_deposit_time_empty_return_deposit_amount_error_empty_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "5",
        "depositTimeMonths": "",
        "bankInterestRate": "3"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositTimeMonthsError": EMPTY_FILED_MESSAGE}


def test_user_deposit_input_form_validation_bank_interest_rate_empty_return_bank_interest_rate_error_empty_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "5",
        "depositTimeMonths": "6",
        "bankInterestRate": ""
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"bankInterestRateError": EMPTY_FILED_MESSAGE}


def test_user_two_fields_empty_rate_then_error_on_this_two_fields_empty_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "",
        "depositTimeMonths": "",
        "bankInterestRate": "7"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositAmountError": EMPTY_FILED_MESSAGE,
                      "depositTimeMonthsError": EMPTY_FILED_MESSAGE
                      }


def test_user_two_other_fields_empty_rate_then_error_on_this_other_two_fields_empty_messages(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "5",
        "depositTimeMonths": "",
        "bankInterestRate": ""
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositTimeMonthsError": EMPTY_FILED_MESSAGE,
                      "bankInterestRateError": EMPTY_FILED_MESSAGE
                      }


def test_deposit_amount_have_letters_then_cannot_have_letters_error_messages_on_this_field(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "34kkLLi",
        "depositTimeMonths": "3",
        "bankInterestRate": "5"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {"depositAmountError": CANNOT_HAVE_LETTERS_MESSAGE}


def test_all_fields_have_letters_then_all_have_letters_error_messages_on_this_fields(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "34kkLLi",
        "depositTimeMonths": "$hht",
        "bankInterestRate": "pouyf"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositAmountError": CANNOT_HAVE_LETTERS_MESSAGE,
        "depositTimeMonthsError": CANNOT_HAVE_LETTERS_MESSAGE,
        "bankInterestRateError": CANNOT_HAVE_LETTERS_MESSAGE
    }


def test_all_fields_have_values_below_zero_then_all_have_bellow_zero_error_messages_on_this_fields(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "-5",
        "depositTimeMonths": "-8",
        "bankInterestRate": "0"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositAmountError": CANNOT_BE_ZERO_OR_BELOW_MESSAGE,
        "depositTimeMonthsError": CANNOT_BE_ZERO_OR_BELOW_MESSAGE,
        "bankInterestRateError": CANNOT_BE_ZERO_OR_BELOW_MESSAGE
    }


def test_field_bank_interest_rate_have_values_above_100_deposit_amount_is_empty_and_deposit_time_months_bellow_zero_then_errors_messages_accordingly(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "",
        "depositTimeMonths": "-8",
        "bankInterestRate": "101"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositAmountError": EMPTY_FILED_MESSAGE,
        "depositTimeMonthsError": CANNOT_BE_ZERO_OR_BELOW_MESSAGE,
        "bankInterestRateError": CANNOT_BE_BIGGER_THAN_100_PERCENT
    }
