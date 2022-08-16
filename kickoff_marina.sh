python /manage.py migrate
python /manage.py makemigrations power
python /manage.py migrate power
python /manage.py createsuperuser --noinput
python manage.py loaddata /marina/power/fixtures/initial.json
python /manage.py runserver 0.0.0.0:8000
