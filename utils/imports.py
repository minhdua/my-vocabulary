import csv
from google.cloud import translate_v2 as translate
import requests


def remove_empty(data):
    rm_keys = []
    for key in data.keys():
        if data[key] == '':
            rm_keys.append(key)
    for key in rm_keys:
        data.pop(key)
    return data


def get_translation(word):
    translate_client = translate.Client()
    return translate_client.translate(word, 'vi')


def get_topic(file_path):
    return {'code': input('unit code >>> '),
            'name': input('unit name >>> '),
            'import_path': file_path}


class ImportCsv:

    def __init__(self, file_path=None, delimiter='|'):
        self.self.file_path = file_path
        self.delimiter = delimiter

    def read_file(self):
        with open(self.self.file_path, encoding='utf8') as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
            csv_reader = csv.reader(csv_file, dialect)
            line_count = 0
            data = []
            for row in csv_reader:
                if line_count == 0:
                    header = row
                else:
                    zip_iterator = zip(header, row)
                    data_dict = dict(zip_iterator)
                    data.append(data_dict)
                line_count += 1
            return data

    def to_vocabularies(self):
        dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'
        data = self.read_file()
        topic = get_topic(self.file_path)
        vocabularies = []
        for d in data:
            d = remove_empty(d)
            word = d.get('word', None)
            if word is not None:
                vocabulary = {}
                vi_definition = d.get('vi_definition', None)
                typeofword = d.get('type', None)
                vocabulary.setdefault('import_path', self.file_path)
                response = requests.get(dictionary_url.format(word))
                if response.status_code == 200:
                    json = response.json()
                    for res in json:
                        res_word = res['word']
                        vocabulary.setdefault('word', res_word)
                        phonetics = res['phonetics']
                        vocabulary.setdefault('phonetics', phonetics)
                        meanings = res['meanings']
                        vocabulary.setdefault('meanings', meanings)
                        translation = get_translation(res_word)
                        translation['vi_definition'] = vi_definition
                        if typeofword is not None:
                            translation['typeOfWord'] = typeofword
                        vocabulary.setdefault('translations', [translation])
                        d.setdefault('topics', {topic['code']})
                        vocabularies.append(vocabulary)
        return vocabularies
