FROM python:3.8
RUN mkdir humansAPI
WORKDIR humansAPI
COPY . .
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
RUN python -m pip install -r requirements.txt
