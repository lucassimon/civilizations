FROM python:3.6-alpine

RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add python3 && \
    apk add python3-dev && \
    apk add py3-pip && \
    apk add build-base && \
    apk add jq && \
    apk add curl && \
    apk add tzdata && \
    apk add git && \
    apk add ca-certificates && \
    update-ca-certificates && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone && \
    pip install awscli && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

RUN adduser -D oyaji
USER oyaji

COPY . /home/oyaji
WORKDIR /home/oyaji

# COPY requirements requirements
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements/docker.txt

# COPY apps apps
# COPY migrations migrations
# COPY application.py celery_worker.py config.py boot.sh ./

RUN chmod a+x ./boot.sh && \
    /usr/bin/make setup

# run-time configuration
CMD ["/home/oyaji/boot.sh"]
