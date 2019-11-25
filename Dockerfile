FROM python:alpine

RUN apk update && apk upgrade && \
    apk add gcc \
            libffi-dev \
            make \
            musl-dev \
            openssl-dev

WORKDIR /opt/buildbot_tyrian_theme
COPY . /opt/buildbot_tyrian_theme

RUN pip install -r requirements.txt && \
    python setup.py install
