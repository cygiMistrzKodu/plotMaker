from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file("intrest_rate_result_view.kv")


class IntrestRateResultView(BoxLayout):
    depositAmount = StringProperty("")
    depositTime = StringProperty("")
    annualInterestRate = StringProperty("")
