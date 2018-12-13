FROM ubuntu:16.04

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install python3 python3-pip python-dev libmysqlclient-dev python3-dev -y
    
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

ENV PYTHONBUFFERED 1
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:3000"]