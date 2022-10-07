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