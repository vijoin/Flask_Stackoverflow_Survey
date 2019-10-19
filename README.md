# Extract information from Stackoverflow Survey 2019

## How to use it
* Download the repository
* Download the source files from [Survey 2019](https://drive.google.com/open?id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV)
  * Place `survey_results_public.csv` into `source/developer_survey_2019/` directory
* Activate the virtualenv
  * source venv/bin/activate
* Run `flask run`

Test with:

Get info using schema titles (case sensitive)

i.e: 

* http://127.0.0.1:5000/question/LanguageWorkedWith
* http://127.0.0.1:5000/question/Country
* http://127.0.0.1:5000/question/Hobbyist
* or any other title in the schema `developer_survey_2019/survey_results_schema.csv`

or

Total by language (case sensitive)

i.e:

* http://127.0.0.1:5000/language/Python
* http://127.0.0.1:5000/language/SQL
* or any other language in `http://127.0.0.1:5000/question/LanguageWorkedWith`