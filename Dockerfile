# pull base image
FROM python:3.11.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install global dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# user
RUN useradd -ms /bin/bash django
RUN mkdir -p /code && chown django:django /code
USER django

# set work directory
WORKDIR /code

# update path
ENV PATH="/home/django/.local/bin:${PATH}"
ENV PYTHONPATH="/code:${PYTHONPATH}"

# setup python environment
COPY requirements.txt /code/
RUN python -m venv /code/.venv
RUN /code/.venv/bin/activate && echo "activated virtual environment"
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# copy project
COPY . /code/