from interfaces.user_deposit import UserDeposit

from validation.user_deposit_validation import UserDepositValidator

import pytest


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


def test_fields_values_above_100_and_is_empty_and_bellow_zero_then_errors_messages_accordingly(
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


def test_empty_dictionary_should_return_on_all_fields_empty_errors_message(
        user_deposit_validator):
    deposit: UserDeposit = {}

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositAmountError": EMPTY_FILED_MESSAGE,
        "depositTimeMonthsError": EMPTY_FILED_MESSAGE,
        "bankInterestRateError": EMPTY_FILED_MESSAGE
    }


def test_one_right_key_in_input_dictionary_should_return_on_rest_fields_empty_errors_message(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "4",
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositTimeMonthsError": EMPTY_FILED_MESSAGE,
        "bankInterestRateError": EMPTY_FILED_MESSAGE
    }


def test_two_right_key_in_input_dictionary_one_is_missing_should_return_empty_errors_message_on_that_filed(
        user_deposit_validator):
    deposit: UserDeposit = {
        "depositAmount": "4",
        "bankInterestRate": "68"
    }

    errors = user_deposit_validator.validate_deposit_form(deposit)

    assert errors == {
        "depositTimeMonthsError": EMPTY_FILED_MESSAGE,
    }
