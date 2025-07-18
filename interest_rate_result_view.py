from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("interest_rate_result_view.kv")


class InterestRateResultView(BoxLayout):
    depositAmount = StringProperty("")
    depositTimeMonths = StringProperty("")
    bankInterestRate = StringProperty("")

    annualIntrestRateIncrease = StringProperty("na rok")
    monthlyIntrestRateIncrease = StringProperty("na miech")
    dailyIntrestRateIncrease = StringProperty("876")

    intrestRateNet = StringProperty("empty")
    intrestRateGross = StringProperty("empty")
