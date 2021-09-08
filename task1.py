import json


class MyIterator:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf-8')
        self.cities_names_list = []

        with open('countries.json') as f:
            file = json.load(f)
            for i in file:
                self.cities_names_list.append(i['name']['common'])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            city = self.cities_names_list.pop(0)
        except IndexError:
            raise StopIteration

        return city


with open('output_file.txt', 'w') as out_file:
    for city in MyIterator('countries.json'):
        try:
            out_file.write(f"{city} : https://wikipedia.org/wiki/{city.replace(' ', '_')}\n")
            print(f"{city} : https://wikipedia.org/wiki/{city.replace(' ', '_')}")
        except UnicodeEncodeError:
            pass