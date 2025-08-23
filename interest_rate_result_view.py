from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("interest_rate_result_view.kv")


class InterestRateResultView(BoxLayout):
    depositAmount = StringProperty("")
    depositTimeMonths = StringProperty("")
    bankInterestRate = StringProperty("")

    annualIntrestRateIncreaseGross = StringProperty("na rok")
    monthlyIntrestRateIncreaseGross = StringProperty("na miech")
    dailyIntrestRateIncreaseGross = StringProperty("876")

    annualIntrestRateIncreaseNet = StringProperty("")
    monthlyIntrestRateIncreaseNet = StringProperty("")
    dailyIntrestRateIncreaseNet = StringProperty("")

    intrestRateNet = StringProperty("empty")
    intrestRateGross = StringProperty("empty")
