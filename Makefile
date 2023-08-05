mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver $(port)

app:
	python3 manage.py startapp $(name)

admin:
	python3 manage.py createsuseruser

coll:
	python3 manage.py collectstatic
