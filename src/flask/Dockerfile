FROM python:3.9.2

WORKDIR /src

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libgl1 musl-dev g++ -y
RUN apt-get install python3-pip -y

COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD [ "uwsgi", "wsgi.ini" ]


