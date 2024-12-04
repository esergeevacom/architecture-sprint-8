FROM python:3.11 AS base

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DEFAULT_TIMEOUT=100

ARG DOCKER_USER_ID=5001

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    locales \
    libfbclient2 && \
    useradd -m -u ${DOCKER_USER_ID} pyworker

ENV TZ 'Europe/Moscow'
RUN echo $TZ > /etc/timezone && apt-get update && \
    apt-get install -y tzdata && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

USER ${DOCKER_USER_ID}
RUN mkdir -p /home/pyworker/app
WORKDIR /home/pyworker/app

ENV PATH "$PATH:/home/pyworker/.local/bin"
ENV PYTHONPATH "."

COPY ./api/container/requirements.txt .

RUN pip install --upgrade pip --no-cache-dir --user -r  requirements.txt

ADD --chown=${DOCKER_USER_ID}  . /home/pyworker/app/
