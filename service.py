import requests
from translate import Translator


# working but too slow
class TranslaterByOne:
    """
    language args:
    ukrainian - ua
    english = en
    russian - pidory
    """

    def __init__(self, text: str, language: str = 'uk'):
        global result
        global counter
        processor = Translator(language, from_lang='en')
        res = processor.translate(text[1:-1])
        result.append(res)
        print(f"{counter}.{text} -> {res}")
        counter += 1

    @staticmethod
    def io_write(data):
        with open('data.json', 'w') as x:
            x.write(str(data))


# working, but too slow and cant be provided
class TranslaterByScope:
    data_string: str

    def __init__(self, language: str = 'uk'):
        print("--- In __init__")
        self.processor = Translator(language)

    @staticmethod
    def data_cleaner(io_string: str):
        print(f"--- In data_cleaner")
        target_string: str = ""
        io_string = eval(io_string)
        for x in io_string:
            target_string.__add__(x[1:-1] + " ")
        return target_string.split(' ')

    def ScopeTranslater(self, data: list):  # noqa
        print(f"--- In {self.ScopeTranslater.__name__}")
        uk_data = ""
        bulk_finish = 5000
        string_for_translate = ""
        temp_string_for_translate = ""
        for x in data:
            temp_string_for_translate.__add__(x)
            if temp_string_for_translate.__len__() >= bulk_finish or data.index(x) == data.__len__() - 1:
                uk_data.__add__(self.processor.translate(string_for_translate))
            else:
                string_for_translate = temp_string_for_translate
        return uk_data


"""
def create_ua_layout():
    with open('new_cities.json', 'r') as x:
        data = x.read()
        data = data[1:-1].split(',')
        for city in data:
            obj = TranslaterByOne(city)
        obj.io_write(result)

obj = TranslaterByScope()
with open('ua_cities.json', 'w') as file:
    file.write(obj.ScopeTranslater(obj.data_cleaner(open('new_cities.json', 'r').read())))

"""


class TranslateInGame:
    def __init__(self, text):
        self.processor = Translator(from_lang='uk', to_lang='en')
        print(f"ORIG: {text}")
        self.result = self.processor.translate(text)
        print(f"TRAN: {self.result}")

    def __str__(self):
        self.result = f"{self.result}"
        return self.result


def cities_upgrade():
    data = open("cities.json", 'r').readlines()
    data_to_json = []
    for x in data:
        if x[:10] == '    "name"':
            x = x.split(":")
            data_to_json.append(x[1][2:-3])
    open("new_cities.json", 'w').write(str(data_to_json))
