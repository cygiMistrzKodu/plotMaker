from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("interest_rate_result_view.kv")


class InterestRateResultView(BoxLayout):
    LABEL_TEXTS = {
        "interest_result_title_label_id": "[u]Deposit (zł)[/u]",
        "deposit_amount_label_id": "Deposit (zł):",
        "deposit_time_months_label_id": "Time (m.):",
        "bank_interest_rate_label_id": "Percent (%):",
        "capital_with_interest_gross_label_id": "Gross profit",
        "capital_with_interest_net_label_id": "Net profit",
        "interest_rate_gross_label_id": "Gross interest",
        "interest_rate_net_label_id": "Net interest",
        "tax_from_interest_rate_label_id": "Tax",
        "gross_daily_interest_rate_label_id": "Gross daily",
        "net_daily_interest_rate_label_id": "Net daily",
        "tax_daily_interest_rate_label_id": "Tax daily",
        "gross_monthly_interest_rate_label_id": "Gross monthly",
        "net_monthly_interest_rate_label_id": "Net monthly",
        "tax_monthly_interest_rate_label_id": "Tax monthly",
        "gross_annual_interest_rate_label_id": "Gross annual",
        "net_annual_interest_rate_label_id": "Net annual",
        "tax_annual_interest_rate_label_id": "Tax annual",

    }

    depositAmount = StringProperty("")
    depositTimeMonths = StringProperty("")
    bankInterestRate = StringProperty("")

    grossCapitalWithInterest = StringProperty("")
    netCapitalWithInterest = StringProperty("")

    annualIntrestRateIncreaseGross = StringProperty("")
    monthlyIntrestRateIncreaseGross = StringProperty()
    dailyIntrestRateIncreaseGross = StringProperty("")

    annualIntrestRateIncreaseNet = StringProperty("")
    monthlyIntrestRateIncreaseNet = StringProperty("")
    dailyIntrestRateIncreaseNet = StringProperty("")

    annualIntrestRateIncreaseTax = StringProperty("")
    monthlyIntrestRateIncreaseTax = StringProperty("")
    dailyIntrestRateIncreaseTax = StringProperty("")

    intrestRateGross = StringProperty("")
    intrestRateNet = StringProperty("")
    intrestRateTax = StringProperty("")

    def translate(self, key: str) -> str:
        return App.get_running_app()._(key)

    def refresh_texts(self):
        for widget_id, raw_text in self.LABEL_TEXTS.items():
            translated_text = self.translate(raw_text)
            if widget_id in self.ids:
                self.ids[widget_id].text = translated_text
