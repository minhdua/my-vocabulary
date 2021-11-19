import csv
from documents.vocabulary import Vocabulary
from documents.translation import Translation
from documents.topic import Topic
from datetime import datetime
from pathlib import Path


def get_folder_path(file_path):
    path = Path(file_path)
    if path.is_file():
        return path.parent
    return path


class ExportCsv:

    def __init__(self, kwargs={}):
        file_path = kwargs.pop('file_path', 'D:/template_csv/')
        self.path = get_folder_path(file_path)
        self.path.mkdir(parents=True, exist_ok=True)
        self.vocabulary = kwargs.pop('vocabulary', Vocabulary())
        self.translation = kwargs.pop('translation', Translation())
        self.topic = kwargs.pop('topic', Topic())

    def export_template(self):
        v_dict = self.vocabulary.__dict__
        tr_dict = self.translation.__dict__
        to_dict = self.topic.__dict__

        ignore_header = ['created_date', 'updated_date', 'id', 'topics', 'translations', 'import_path']
        header_row = set().union(v_dict.keys(), tr_dict.keys(), to_dict.keys())
        for header in ignore_header:
            header_row.remove(header)

        current = datetime.now()
        units_time = [current.year, current.month, current.day, current.hour, current.minute, current.second,
                      current.microsecond]
        file_name = ''.join([str(u) for u in units_time]) + '.csv'

        with open(self.path.joinpath(file_name), 'w', encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file, delimiter='|')
            writer.writerow(header_row)
