import gettext

def set_language(lanc_code):
    locale_path = 'locales'
    lang = gettext.translation('messages', localedir=locale_path, languages=[lanc_code])
    lang.install()
    return lang.gettext
