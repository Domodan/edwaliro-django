# syntax=docker/dockerfile:1

# pull official base image
FROM python:3.8-slim-buster

# set environment variables
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

