# Django development commands

# Install dependencies
sync:
    uv sync --extra dev

# Run Django development server
dev:
    uv run --all-extras manage.py runserver

# Run Django management commands
manage *args:
    uv run manage.py {{args}}

# Run Django migrations
migrate:
    uv run manage.py migrate

# Create new migrations
makemigrations:
    uv run manage.py makemigrations

# Create superuser
createsuperuser:
    uv run manage.py createsuperuser

# Collect static files
collectstatic:
    uv run manage.py collectstatic --noinput

# Run tests
test:
    uv run manage.py test

# Run Django shell
shell:
    uv run manage.py shell

# Show available commands
help:
    @just --list 
