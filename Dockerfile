FROM python:3.6-alpine3.8

ENV PYTHONUNBUFFERED 1
ENV DEBUG '1'

WORKDIR /CRMfood

RUN apk --no-cache add nginx

RUN python3 -m pip install honcho --no-cache-dir

RUN apk add --no-cache --virtual .uwsgi-build-deps \
        gcc \
        musl-dev \
        linux-headers && \
    python3 -m pip install uwsgi --no-cache-dir && \
    apk --purge del .uwsgi-build-deps;

RUN apk add --no-cache openssl
ENV DOCKERIZE_VERSION v0.6.1
RUN wget "https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz" \
    && rm "dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz"

COPY requirements.txt .

RUN apk --no-cache add \
        postgresql-libs && \
    apk --no-cache add \
        --virtual .requirements-build-deps \
        gcc \
        musl-dev \
        libffi-dev \
        postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .requirements-build-deps

COPY . .

RUN  mkdir -p /run/nginx/
COPY docker/nginx-app.conf /etc/nginx/conf.d/default.conf
COPY docker/uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY docker/uwsgi_params /etc/nginx/uwsgi_params

EXPOSE 8000

ENTRYPOINT [ "/code/entrypoint.sh" ]
CMD [ "/usr/local/bin/honcho", "-f", "/code/docker/Procfile", "start" ]