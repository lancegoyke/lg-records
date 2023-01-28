# Record

Compete with others and climb to the top of the leaderboard! 🚀

I wrote this Django app to store metabolic workouts and keep track of how my clients were performing.

I managed to keep it simple:

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

To spin up development server:

```
sudo docker compose up -d --build
```

To spin down development serve:

```
sudo docker compose down
```

The database will need to be set up as well:

```
sudo docker compose exec web python manage.py migrate
```

## Deploying for Production

This project is deployed on heroku. You can push directly to heroku:

```
heroku login
git push heroku master
```

The `heroku.yml` file runs two commands in the release phase:

```
python manage.py migrate  # untested
python manage.py collectstatic --noinput
```

If you need to run commands on the production server, check out `heroku run` from the Heroku CLI.
