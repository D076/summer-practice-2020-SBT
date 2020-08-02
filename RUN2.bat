pip install -r requirements.txt
set APP_SETTINGS=config.DevelopmentConfig
set DATABASE_URL=sqlite:///test.db
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver