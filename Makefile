.PHONY:
.PHONY:
run_bot:
	pdm run python run.py
	

.PHONY:
runserver:
	pdm run python manage.py runserver 5000


.PHONY:
migrate:
	pdm run python manage.py migrate


.PHONY:
makemigrations:
	pdm run python manage.py makemigrations

.PHONY:
shell:
	pdm run python manage.py shell