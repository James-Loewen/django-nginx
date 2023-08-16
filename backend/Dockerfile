FROM python:slim-bullseye

WORKDIR /home/app

COPY requirements.txt .
RUN \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]