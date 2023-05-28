.PHONY:
run:
	pdm run python manage.py runserver 5000


.PHONY:
migrate:
	pdm run python manage.py migrate


.PHONY:
makemigrations:
	pdm run python manage.py makemigrations