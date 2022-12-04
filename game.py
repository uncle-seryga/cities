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

    def if_used(self):
        pass

    def if_last_letter(self):
        pass


class Multiplayer:
    pass


class Anticheat:
    pass
