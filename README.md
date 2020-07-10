
# Introduction

[Original Idea](https://github.com/dennyzhang/monitor-docker-slack)

Get Slack and Telegram notifications, when specific container status is defined.


# How to use

Create the next enviroment variables to configure notifications.

```
NOTIFY_STATUS="created,restarting,running,paused,exited"
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

```
docker run   -v  /var/run/docker.sock:/var/run/docker.sock -e "NOTIFY_STATUS='created,restarting,running,paused,exited" -e "TIMEOUT=10" silvelo/docker_notify
```
## docker-compose

```
version: "3"

services:
  docker-notify:
    image: silvelo/docker_notify:latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      TELGRAM_TOKEN: ""
      TELEGRAM_CHAT_ID: ""
      SLACK_HOOK_URL: ""
      NOTIFY_STATUS: "created,restarting,running,paused,exited"
      TIME_OUT: 10
    
```

