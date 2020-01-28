FROM python:3.8

RUN mkdir /app
WORKDIR /app

# INSTALL DEPENDENCIES
COPY ./requeriments.txt /app

RUN pip install -r requeriments.txt

EXPOSE 8080