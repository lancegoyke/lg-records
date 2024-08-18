# pull base image
FROM python:3.11.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# user
RUN useradd -ms /bin/bash django
USER django


# set work directory
WORKDIR /code

# install global dependencies
USER root
RUN apt-get update && apt-get install -y libpq-dev gcc

# update path
USER django
ENV PATH="/home/django/.local/bin:${PATH}"
ENV PYTHONPATH="/code:${PYTHONPATH}"

# setup python environment
COPY requirements.txt /code/
# RUN python -m venv /code/.venv
# RUN source /code/.venv/bin/activate
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# copy project
COPY . /code/