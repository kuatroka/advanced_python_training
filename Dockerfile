# FROM python:latest
# FROM sql_training_linux_machine
FROM python:3.9.7-slim-buster

RUN apt update && apt upgrade -y



# COPY . /code
# WORKDIR /code


ENTRYPOINT ["/bin/bash"]




