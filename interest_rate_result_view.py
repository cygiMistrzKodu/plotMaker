from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("interest_rate_result_view.kv")


class InterestRateResultView(BoxLayout):
    depositAmount = StringProperty("")
    depositTimeMonths = StringProperty("")
    bankInterestRate = StringProperty("")

    annualIntrestRateIncreaseGross = StringProperty("")
    monthlyIntrestRateIncreaseGross = StringProperty()
    dailyIntrestRateIncreaseGross = StringProperty("")

    annualIntrestRateIncreaseNet = StringProperty("")
    monthlyIntrestRateIncreaseNet = StringProperty("")
    dailyIntrestRateIncreaseNet = StringProperty("")

    annualIntrestRateIncreaseTax = StringProperty("")
    monthlyIntrestRateIncreaseTax = StringProperty("")
    dailyIntrestRateIncreaseTax = StringProperty("")

    intrestRateNet = StringProperty("empty")
    intrestRateGross = StringProperty("empty")
