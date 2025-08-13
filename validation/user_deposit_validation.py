from decimal import Decimal, InvalidOperation
from interfaces.user_deposit import UserDeposit


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

        deposit = self._fill_missing_keys(deposit, ["depositAmount", "depositTimeMonths", "bankInterestRate"])

        errors: dict[str, str] = {"depositAmountError": self.validate_deposit_amount(deposit["depositAmount"]),
                                  "depositTimeMonthsError": self.validate_deposit_time(deposit["depositTimeMonths"]),
                                  "bankInterestRateError": self.validate_bank_interest_rate(
                                      deposit["bankInterestRate"])}

        errors = self._remove_keys_with_none(errors)

        return errors if errors else None

    def _fill_missing_keys(self, data: UserDeposit, require_keys: list[str]) -> UserDeposit:
        for key in require_keys:
            data.setdefault(key, "")
        return data

    def _remove_keys_with_none(self, errors):
        errors = {key: value for key, value in errors.items() if
                  value is not None}
        return errors
