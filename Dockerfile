FROM python:3.10-slim-buster

WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 31216

CMD [ "python3", "task2.py"]