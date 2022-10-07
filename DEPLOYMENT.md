# Games Exclusives - deployment

## GitHub
## Workspace Setup
## Stripe
## Emails
## Heroku
 pip3 install dj_database_url
 pip3 install psycopg2-binary
  pip3 freeze > requirements.txt
  python3 manage.py migrate
  python3 manage.py loaddata categories
  python3 manage.py loaddata games
  python3 manage.py createsuperuser
  pip3 install gunicorn
   pip3 freeze > requirements.txt
   heroku login -i (email and API as password)
   heroku config:set DISABLE_COLLECTSTATIC=1 -a, --app games-exclusives
   heroku git:remote -a games-exclusives
   git push heroku main
   --> error
   touch runtime.txt && echo "python-3.9.14" > runtime.txt
   git add . && git commit -m "Add runtime.txt for heroku deployment"
   git push
   git push origin main
   heroku stack:set heroku-20 -a games-exclusives
   git push heroku main
   remove secret key from settings and replace with os.environ.get('SECRET_KEY', '')
   add secret key in settings on heroku
   set DEBUG to DEBUG = 'DEVELOPMENT' in os.environ