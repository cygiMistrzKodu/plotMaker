from decimal import Decimal


class InterestRateCalculator:
    def __init__(self, amount: str, months: str, interest_rate: str):
        self.amount = Decimal(amount)
        self.months = Decimal(months)
        self.interest_rate = Decimal(interest_rate)

    def calculate(self):
        gross = self.amount * (self.interest_rate / 100) * self.months / 12
        tax_from_income_percent = Decimal(0.19)
        tax_amount_from_interest = gross * tax_from_income_percent
        net = gross - tax_amount_from_interest

        annual_increase_gross = self.amount * (self.interest_rate / 100)
        tax_from_annual_increase = tax_from_income_percent * annual_increase_gross
        annual_increase_net = annual_increase_gross - tax_from_annual_increase

        monthly_increase_gross = self.amount * (self.interest_rate / 100) / 12
        tax_from_monthly_increase = tax_from_income_percent * monthly_increase_gross
        monthly_increase_net = monthly_increase_gross - tax_from_monthly_increase

        daily_increase_gross = self.amount * (self.interest_rate / 100) / 365
        tax_from_daily_increase = tax_from_income_percent * daily_increase_gross
        daily_increase_net = daily_increase_gross - tax_from_daily_increase

        return {
            "depositAmount": f"{self.amount}",
            "depositTimeMonths": f"{self.months}",
            "bankInterestRate": f"{self.interest_rate}",
            "intrestRateGross": f"{gross:.3f}",
            "intrestRateNet": f"{net:.3f}",
            "intrestRateTax": f"{tax_amount_from_interest:.3f}",
            "annualIntrestRateIncreaseGross": f"{annual_increase_gross:.3f}",
            "annualIntrestRateIncreaseNet": f"{annual_increase_net:.3f}",
            "annualIntrestRateIncreaseTax": f"{tax_from_annual_increase:.3f}",
            "monthlyIntrestRateIncreaseGross": f"{monthly_increase_gross:.3f}",
            "monthlyIntrestRateIncreaseNet": f"{monthly_increase_net:.3f}",
            "monthlyIntrestRateIncreaseTax": f"{tax_from_monthly_increase:.3f}",
            "dailyIntrestRateIncreaseGross": f"{daily_increase_gross:.3f}",
            "dailyIntrestRateIncreaseNet": f"{daily_increase_net:.3f}",
            "dailyIntrestRateIncreaseTax": f"{tax_from_daily_increase:.3f}"
        }
