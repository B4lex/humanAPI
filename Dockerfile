FROM python:latest
RUN mkdir humansAPI
WORKDIR humansAPI
COPY ./src .
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
RUN python -m pip install -r requirements.txt
