FROM python:3.6
LABEL maintainer="Pablo Vieira <povieira@gmail.com>"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -e . && pip install -r requirements_dev.txt
