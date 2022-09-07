import json


class Utils:
    """---> class создал новый экземпляр класса!\n"""

    def __init__(self, id_=None, name=None, picture=None, position=None, gender=None, age=None, skills=None):
        print(self.__class__.__name__, self.__doc__)
        self.path = None  # Загруженные данные из файла
        self.id_ = id_
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills
        self.arr = []  # список всех кандидатов

    def load_candidates(self, filename):
        """ Загружает данные из файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            self.path = json.load(f)
        return self.path

    def load_candidates_from_json(self):
        """Показывает всех кандидатов"""
        for item in self.path:
            self.arr.append(
                Utils(item['id'], item['name'], item['picture'], item['position'], item['gender'], item['age'],
                      item['skills']))
        return self.arr

    def get_candidate(self, candidate_id):
        """Вернет кандидата по pk"""
        for item in self.arr:
            if item.id_ == int(candidate_id):
                return item


    def get_candidates_by_name(self, candidate_name: str) -> list:
        """Вернет кандидатов по имени"""
        arr_candidate_name = []  # Список кандидатов по навыку
        for item in self.arr:
            for i in [item.name.lower()]:
                if candidate_name.lower() in i:
                    arr_candidate_name.append(item)
        return arr_candidate_name

    def get_candidates_by_skill(self, skill_name: str) -> list:
        """Вернет кандидатов по навыку"""
        arr_skill_name = []  # Список кандидатов по навыку
        for item in self.arr:
            for i in [item.skills.lower()]:
                if skill_name.lower() in i:
                    arr_skill_name.append(item)
        return arr_skill_name

    def __repr__(self):
        return f"{self.id_} {self.name} {self.picture} {self.position} {self.gender} {self.age} {self.skills}"

    def __str__(self):
        return f"{self.id_} {self.name} {self.picture} {self.position} {self.gender} {self.age} {self.skills}"


""" Для тестирования работы функций"""
#
# req = Utils()
#
# req.load_candidates('candidates.json')
#
# print(req.load_candidates_from_json())
#
# print(req.get_candidate(2))
#
# print(req.get_candidates_by_skill('python'))
#
# print(req.get_candidates_by_name('Stein'))
#
# print(len(req.get_candidates_by_name('Adela Hendricks')))