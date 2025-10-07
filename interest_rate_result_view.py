from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("interest_rate_result_view.kv")


class InterestRateResultView(BoxLayout):
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
        labels_translations = {
            "interest_result_title_id": self.translate("[u]Deposit (zł)[/u]"),
        }
        for widget_id, translated_text in labels_translations.items():
            if widget_id in self.ids:
                self.ids[widget_id].text = translated_text
