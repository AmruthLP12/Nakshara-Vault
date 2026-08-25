PORT ?= 7000


run :
	uv run manage.py runserver 0.0.0.0:$(PORT)

migrate :
	uv run manage.py migrate

makemigrations :
	uv run manage.py makemigrations

update_index :
	uv run manage.py update_index

createsuperuser :
	uv run manage.py createsuperuser

shell :	
	uv run manage.py shell

libretranslate:
	uv run libretranslate --host 127.0.0.1 --port 7001