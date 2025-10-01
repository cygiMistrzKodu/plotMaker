from decimal import Decimal, InvalidOperation
from interfaces.user_deposit import UserDeposit


class UserDepositValidator:
    EMPTY_FILED_KEY = "field_cannot_be_empty"
    CANNOT_HAVE_LETTERS_KEY = "filed_cannot_have_letters"
    CANNOT_BE_ZERO_OR_BELOW_KEY = "filed_cannot_be_less_or_equal_to_zero"
    CANNOT_BE_BIGGER_THAN_100_KEY = "filed_cannot_be_bigger_than_100%"

    def _validate_decimal(self, value) -> str | None:
        try:
            Decimal(value)
        except InvalidOperation:
            return self.CANNOT_HAVE_LETTERS_KEY

    def _validate_decimal_above_zero(self, value) -> str | None:
        if Decimal(value) <= Decimal("0"):
            return self.CANNOT_BE_ZERO_OR_BELOW_KEY
        return None

    def _validate_filed_not_empty(self, value) -> str | None:
        if value == "":
            return self.EMPTY_FILED_KEY
        return None

    def validate_deposit_amount(self,
                                amount: str):

        error_key = self._validate_filed_not_empty(amount)
        if error_key:
            return error_key

        error_key = self._validate_decimal(amount)
        if error_key:
            return error_key

        error_key = self._validate_decimal_above_zero(amount)
        if error_key:
            return error_key

        return None

    def validate_deposit_time(self, time: str):

        if time == "":
            return self.EMPTY_FILED_KEY

        error = self._validate_decimal(time)
        if error:
            return error

        error = self._validate_decimal_above_zero(time)
        if error:
            return error

        return None

    def validate_bank_interest_rate(self, bank_interest_rate):

        if bank_interest_rate == "":
            return self.EMPTY_FILED_KEY

        error_key = self._validate_decimal(bank_interest_rate)
        if error_key:
            return error_key

        error_key = self._validate_decimal_above_zero(bank_interest_rate)
        if error_key:
            return error_key

        if Decimal(bank_interest_rate) > Decimal(100):
            return self.CANNOT_BE_BIGGER_THAN_100_KEY

        return None

    def validate_deposit_form(self, deposit: UserDeposit) -> None | dict[str, str]:

        deposit = self._fill_missing_keys(deposit, ["depositAmount", "depositTimeMonths", "bankInterestRate"])

        errors_key: dict[str, str] = {"depositAmountErrorKey": self.validate_deposit_amount(deposit["depositAmount"]),
                                  "depositTimeMonthsErrorKey": self.validate_deposit_time(deposit["depositTimeMonths"]),
                                  "bankInterestRateErrorKey": self.validate_bank_interest_rate(
                                      deposit["bankInterestRate"])}

        errors_key = self._remove_keys_with_none(errors_key)

        return errors_key if errors_key else None

    def _fill_missing_keys(self, data: UserDeposit, require_keys: list[str]) -> UserDeposit:
        for key in require_keys:
            data.setdefault(key, "")
        return data

    def _remove_keys_with_none(self, errors_key):
        errors_key = {key: value for key, value in errors_key.items() if
                      value is not None}
        return errors_key
