# pull base image
FROM python:3.11.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# user
RUN useradd -ms /bin/bash django
USER django

# update path
ENV PATH="/home/django/.local/bin:${PATH}"

# set work directory
WORKDIR /code

# install dependencies
USER root
RUN apt-get update && apt-get install -y libpq-dev gcc

USER django
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . /code/