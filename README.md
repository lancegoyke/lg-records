# Record

Compete with others and climb to the top of the leaderboard! 🚀

I wrote this Django app to store metabolic workouts and keep track of how my clients were performing.

## User Flow

1. Sign up for an account
2. View a workout in plain text
3. Time how long it takes you to perform
4. Upload your score

The backend then shows the top score, and, more importantly, _your_ top score. That way you can keep track of what you've done in the past.

It's been surprisingly useful! You're welcome to use it!

[Living Room Glacier (Level 4)](https://record.lancegoyke.com/challenges/living-room-glacier-l4) is probably the hardest one! 😁

## Tech Stack

- Python
- Django
- Docker
- PostgreSQL
- Bulma for styling

## Local Development

First, set up environment variables:

```bash
cp docker-compose.override.yml.example docker-compose.override.yml
# then replace the values with working values
```

To spin up Django development server:

```bash
docker compose up -d --build
```

To spin down development server:

```bash
docker compose down
```

The database will need to be set up as well:

```bash
docker compose exec web python manage.py migrate
```

To create an admin user:

```bash
docker compose exec web python manage.py createsuperuser
```

To login to the Django admin, visit http://127.0.0.1:8000/backside/

Some functionality won't work unless you update the sites model at http://127.0.0.1:8000/backside/sites/site/1/change/

If you ever add or update the Django models, you'll need to instruct Django to update the database with migrations:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

## Deploying for Production

This project is deployed on heroku. You can push directly to heroku:

```bash
heroku login
git push heroku master
```

The `heroku.yml` file runs two commands in the release phase:

```bash
python manage.py migrate  # untested
python manage.py collectstatic --noinput
```

If you need to run commands on the production server, check out `heroku run` from the Heroku CLI.
