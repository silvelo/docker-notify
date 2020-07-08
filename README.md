
# Introduction

[Original Idea](https://github.com/dennyzhang/monitor-docker-slack)

Get Slack and Telegram notifications, when specific container status is defined.


# How to use

Create the next enviroment variables to configure notifications.

```
NOTIFY_STATUS=['created','restarting','running','paused','exited']
TIMEOUT=10
```

## SLACK

For slack notifications configure next enviroment variables
```
SLACK_HOOK_URL=
```

## TELEGRAM

For telegram notifications configure next enviroment variables
```
TELGRAM_TOKEN=
TELEGRAM_CHAT_ID=
```

# Docker

## docker-compose
If you are in windows mount the volume, if not ignore it.
```
version: "3"

services:
  docker-notify:
    image: docker_notify:latest
    environment:
      NOTIFY_STATUS: ['created','restarting','running','paused','exited']
      TIMEOUT: 10
    restart: on-failure
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

```
