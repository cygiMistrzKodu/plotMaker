from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

from i18n.i18n import set_language


class LanguageSelector(BoxLayout):
    def change_language(self, lang_code):
        app = App.get_running_app()
        app._ = set_language(lang_code)

        if hasattr(app.root, 'refresh_texts'):
            app.root.refresh_texts()
