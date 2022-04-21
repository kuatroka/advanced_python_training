# FROM python:latest
FROM sql_training_linux_machine
RUN apt-get update && apt-get install -y bash curl python3.9 python3-pip


# COPY . /code
# WORKDIR /code


ENTRYPOINT ["/bin/bash"]




