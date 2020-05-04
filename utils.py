from collections import defaultdict


def get_language(lang_code):
    langs = defaultdict(lambda: 'fa')
    return langs[lang_code.split("-")[0]] if lang_code else 'fa'
