from interest_rate.calculator import InterestRateCalculator

def test_user_deposit_input_are_add_to_result():
    calc = InterestRateCalculator("10000", "12", "5")
    result = calc.calculate()
    assert result["depositAmount"] == "10000"
    assert result["depositTimeMonths"] == "12"
    assert result["bankInterestRate"] == "5"


def test_calculate_interest_rate_gross_and_net_and_tax_10000_12_5():
    calc = InterestRateCalculator("10000", "12", "5")
    result = calc.calculate()
    assert result["intrestRateGross"] == "500.000"
    assert result["intrestRateNet"] == "405.000"
    assert result["intrestRateTax"] == "95.000"


def test_calculate_interest_rate_gross_and_net_500_6_8():
    calc = InterestRateCalculator("500", "6", "8")
    result = calc.calculate()
    assert result["intrestRateGross"] == "20.000"
    assert result["intrestRateNet"] == "16.200"
    assert result["intrestRateTax"] == "3.800"

def test_can_calculate_annual_increase_in_interest_rate_gross():
    calc = InterestRateCalculator("10000", "12", "5")
    result = calc.calculate()
    assert result["annualIntrestRateIncreaseGross"] == "500.000"

def test_can_calculate_annual_increase_in_interest_rate_net():
    calc = InterestRateCalculator("10000", "12", "5")
    result = calc.calculate()
    assert result["annualIntrestRateIncreaseNet"] == "405.000"

def test_can_calculate_tax_from_annual_increase_in_interest_rate():
    calc = InterestRateCalculator("10000", "12", "5")
    result = calc.calculate()
    assert result["annualIntrestRateIncreaseTax"] == "95.000"

def test_can_calculate_monthly_increase_in_interest_rate_gross():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["monthlyIntrestRateIncreaseGross"] == "1500.000"

def test_can_calculate_monthly_increase_in_interest_rate_net():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["monthlyIntrestRateIncreaseNet"] == "1215.000"

def test_can_calculate_tax_from_monthly_increase_in_interest_rate():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["monthlyIntrestRateIncreaseTax"] == "285.000"

def test_can_calculate_daily_increase_in_interest_rate_gross():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["dailyIntrestRateIncreaseGross"] == "49.315"

def test_can_calculate_daily_increase_in_interest_rate_net():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["dailyIntrestRateIncreaseNet"] == "39.945"

def test_can_calculate_tax_from_daily_increase_in_interest_rate():
    calc = InterestRateCalculator("450000", "6", "4")
    result = calc.calculate()
    assert result["dailyIntrestRateIncreaseTax"] == "9.370"
