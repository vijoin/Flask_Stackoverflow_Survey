import csv
from collections import Counter
from app import app


@app.route('/')
def index():
    return "Hello World"


@app.route('/language/<language>')
def get_results_by_language(language):

    with open('source/developer_survey_2019/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        language_counter = Counter()

        for _, line in zip(range(1, 10), csv_reader):
            languages = line['LanguageWorkedWith'].split(';')
            language_counter.update(languages)

    return f'{language}: {language_counter[language]}'


@app.route('/question/<question>')
def get_results_by_question(question):
    """Use the titles in the schema"""

    with open('source/developer_survey_2019/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = Counter()

        for _, line in zip(range(1, 10), csv_reader):
            counts[line[question]] += 1

    return f"{counts}"
