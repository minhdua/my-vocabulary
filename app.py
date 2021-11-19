from utils.imports import ImportCsv
from connections.firestore_connector import FireStore
from constants.enums.collections import Collection
from documents.topic import Topic
from documents.vocabulary import Vocabulary
from utils.stuffs import to_dict
from documents.translation import Translation
from goslate import Goslate
from constants.enums.languages import Language
from nltk.stem import PorterStemmer
from constants.enums.type_of_word import from_short_name
from google.cloud import translate_v2 as translate
import copy
import requests





def main():

    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'
    file_path = 'D:/data_csv/909TOEIC1.csv'
    importer = ImportCsv(file_path)
    data = importer.read_file()
    topic = get_topic(file_path)
    vocabularies = []
    for d in data:
        d = remove_empty(d)
        word = d.get('word', None)
        if word is not None:
            vocabulary = {}
            vi_definition = d.get('vi_definition', None)
            typeofword = d.get('type', None)
            vocabulary.setdefault('import_path', file_path)
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
                    vocabulary.setdefault('translation', translation)
                    d.setdefault('topics', {topic['code']})
                    vocabularies.append(vocabulary)
    print(vocabularies)


if __name__ == '__main__':
    main()
