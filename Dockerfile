FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get -y install software-properties-common build-essential netcat cron supervisor git less nano vim && \
    apt-add-repository contrib && apt-add-repository non-free && \
    apt-get update
RUN mkdir /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install Cython
RUN pip install -r requirements.txt
COPY . .