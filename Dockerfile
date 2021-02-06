FROM python:latest

RUN git clone https://github.com/vishnubob/wait-for-it.git /wait-for-it
RUN chmod +x /wait-for-it/wait-for-it.sh
RUN mkdir humanAPI
COPY . ./humanAPI
WORKDIR /humanAPI
RUN python -m pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT /wait-for-it/wait-for-it.sh db:5432 && python3 src/randomuser_api_script.py && flask run --host=0.0.0.0