### Basic example of Python application with RabbitMQ and docker compose

#### Usage

##### Run with docker compose

```sh
 cd rabbitmq-with-python-and-docker
 docker-compose up -d --build
```

##### Enter the Pyhton container, to execute the send.py and receive.py scripts 

```sh
 docker exec -it app_python bash && python send.py && python receive.py
```