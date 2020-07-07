FROM amd64/python:3.7-buster

LABEL maintainer="Arturo Silvelo arturo.silvelo@gmail.com"
LABEL version="1.0"
LABEL description="Notify status for docker"

ENV LOGGER_NAME="docker_notify"

WORKDIR /usr/src/app

COPY requirements.txt ./

VOLUME /var/run/docker.sock /var/run/docker.sock

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "docker_notify.py"]