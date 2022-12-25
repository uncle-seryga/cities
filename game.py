import register
import service


class Rules:
    message = "Everything is fine!"

    def __if_city(self, text):
        text = service.TranslateInGame(text)
        with open('new_cities.json', 'r') as file:
            data = eval(file.read())
            if str(text) in data:
                return True
            else:
                self.message = f"City '{text}' not in base"
                return False

    def __if_used(self, this_word):
        """Author - Kirigaya Kazuto from Cherkasy"""
        with open("nado.json", "r") as file:
            data: list = eval(file.read())
            if this_word in data:
                return True
            else:
                self.message = f"City {this_word} is already used"
                return False

    def __if_last_letter(self, last_word, this_word):
        """Author - Kirigaya Kazuto"""
        nado = last_word[-1]
        if nado == "ь":
            nado = last_word[-2]
        if this_word[0].upper() == nado.upper():
            return True
        else:
            self.message = "You dont repeat last letter"
            return False

    def checker(self, city_name):
        results = [self.__if_used(city_name), self.__if_city(city_name),
                   self.__if_last_letter(last_word="", this_word=city_name)]
        if results.count(True) == 3:
            return True
        else:
            return False


class Multiplayer:
    def start_room(self, room_size):
        f = open('sessions/game.json', 'r')
        data: dict = eval(f.read())
        for x in register.Database().get_all_players():
            new = {x[2]: {"name": x[1], "status": 0, "timestamp": 0}}
            data["players"].update(new)
        f = open('sessions/game.json', 'w')
        f.write(str(data))
        def turn(self):
            pass

        def timer(self):
            pass

    class Anticheat:
        pass
