# syntax=docker/dockerfile:1.4

FROM python:slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
COPY . .

# I don't think command will ever be used...
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]