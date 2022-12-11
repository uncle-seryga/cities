import service


class Rules:
    def if_city(self, text):
        text = service.TranslateInGame(text)
        with open('new_cities.json', 'r') as file:
            data = eval(file.read())
            if str(text) in data:
                return True
            else:
                return False

    def if_used(self, this_word):
        """Author - Kirigaya Kazuto from Cherkasy"""
        with open("nado.json", "r") as file:
            data: list = eval(file.read())
            if this_word in data:
                return True
            else:
                return False

    @staticmethod
    def if_last_letter(last_word, this_word):
        """Author - Kirigaya Kazuto"""
        nado = last_word[-1]
        if nado == "ь":
            nado = last_word[-2]
        if this_word[0].upper() == nado.upper():
            return True
        else:
            return False


class Multiplayer:
    def start_room(self):
        pass
    def turn(self):
        pass

    def timer(self):
        pass




class Anticheat:
    pass
