./manage.py reset main && ./manage.py loaddata main_dump.json && python main/text.py --generate-submodels-for-all-texts && ./runserver.sh
