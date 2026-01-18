default:
	@øjust -l

install-requirements:
	pip install -r requirements.txt 

	
serve:
	python manage.py runserver
run: serve

create-password-hash:
	PYTHONPATH=. bin/create-hashed-password.py 


remove-database-data:
	echo "==> Removing all data from the database..."
	python manage.py flush --noinput

loading-user-fixtures:
	python manage.py loaddata snippets/fixtures/users.json

loading-snippets-fixtures:
	python manage.py loaddata snippets/fixtures/snippets.json
