from decimal import Decimal, InvalidOperation  #

import pytest


class UserDepositValidator:
    EMPTY_FILED_MESSAGE = "field cannot be empty"
    CANNOT_HAVE_LETTERS_MESSAGE = "filed cannot have letters"
    CANNOT_BE_ZERO_OR_BELOW_MESSAGE = "filed cannot be less of equal to zero"
    CANNOT_BE_BIGGER_THAN_100_PERCENT = "filed cannot be bigger than 100%"

    def validate_decimal(self, value) -> str | None:
        try:
            Decimal(value)
        except InvalidOperation:
            return self.CANNOT_HAVE_LETTERS_MESSAGE

    def validate_decimal_above_zero(self, value) -> str | None:
        if Decimal(value) <= Decimal("0"):
            return self.CANNOT_BE_ZERO_OR_BELOW_MESSAGE
        return None

    def validate_filed_not_empty(self, value) -> str | None:
        if value == "":
            return self.EMPTY_FILED_MESSAGE
        return None

    def validate_deposit_amount(self,
                                amount: str):

        error = self.validate_filed_not_empty(amount)
        if error:
            return error

        error = self.validate_decimal(amount)
        if error:
            return error

        error = self.validate_decimal_above_zero(amount)
        if error:
            return error

        return None

    def validate_deposit_time(self, time: str):

        if time == "":
            return self.EMPTY_FILED_MESSAGE

        error = self.validate_decimal(time)
        if error:
            return error

        error = self.validate_decimal_above_zero(time)
        if error:
            return error

        return None

    def validate_bank_interest_rate(self, bank_interest_rate):

        if bank_interest_rate == "":
            return self.EMPTY_FILED_MESSAGE

        error = self.validate_decimal(bank_interest_rate)
        if error:
            return error

        error = self.validate_decimal_above_zero(bank_interest_rate)
        if error:
            return error

        if Decimal(bank_interest_rate) > Decimal(100):
            return self.CANNOT_BE_BIGGER_THAN_100_PERCENT

        return None


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
